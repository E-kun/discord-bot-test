import discord
import os
import json
from discord.ext import commands
from discord.ext.commands import BucketType, cog, BadArgument, command, cooldown
from utility.embedconfig import EmbedClass
from utility.nickname_checker import check_nickname
from utility.wep_pagination import WeaponPageView

class Weapons(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()

    def retrieve_weapon(self, weapon):
        with open('data/weapons.json') as file:
            parsed_json = json.load(file)
        return parsed_json[weapon]

    def retrieve_weapontype(self, weapontype):
        with open('data/weapontypes.json') as file:
            parsed_json = json.load(file)
        return parsed_json[weapontype]

    def does_weapon_exist(self, weapon_name):
        with open('data/weaponlist.json') as file:
            parsed_json = json.load(file)

        weaponlist = parsed_json['weaponlist']
        exists = False

        for i in weaponlist:
            if weapon_name == i:
                exists = True
                break
            else:
                exists = False

        return exists

    @commands.Cog.listener()
    async def on_ready(self):
        print('Weapons loaded.')

    @commands.command(aliases=["sig", "wep", "weap"])
    async def weapon(self, ctx: commands.Context, *args) -> None:
        weapon_name = ""
        weapon_box = []

        if len(args) > 1:
            for idx, arg in enumerate(args):
                if(idx) == 0:
                    weapon_name =  weapon_name + args[idx]
                else:
                    weapon_name =  weapon_name + " " + args[idx]
        else:
            weapon_name = args[0]
        
        print(weapon_name)

        if(self.does_weapon_exist(weapon_name)):
            weapon = self.retrieve_weapon(weapon_name)
            embed = self.embedconf.create_weapon_embed(weapon)
            await ctx.send(embed=embed)
        elif(not(self.does_weapon_exist(weapon_name))):
            weapon_name = check_nickname(weapon_name, "weapon")  
            if(self.does_weapon_exist(weapon_name)):
                weapon = self.retrieve_weapon(weapon_name)
                weapontype = weapon['weapon_type']
                same_type_weapons_list = self.retrieve_weapontype(weapontype.lower())

                for i in same_type_weapons_list:
                    if(self.retrieve_weapon(i)['rarity'] < 6):
                        weapon_box.append(self.retrieve_weapon(i))

                weapon_box.append(weapon)

                embed = self.embedconf.create_weapon_embed(weapon)
                view = WeaponPageView(ctx.author, weapon_box=weapon_box)
                await ctx.send(view=view, embed=embed)
            else:
                content = "This weapon does not exist. Please try again."
                await ctx.send(content=content)
        else:
            content = "This weapon does not exist. Please try again."
            await ctx.send(content=content)


async def setup(bot: commands.Bot):
    await bot.add_cog(Weapons(bot))

async def teardown(bot):
    print("Extension unloaded!")
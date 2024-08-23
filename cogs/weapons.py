import discord
import os
import json
from discord.ext import commands
from discord.ext.commands import BucketType, cog, BadArgument, command, cooldown
from embedconfig import EmbedClass

class Weapons(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()

    def retrieve_weapon(self, weapon):
        with open('data/weapons.json') as file:
            parsed_json = json.load(file)
        return parsed_json[weapon]

    def does_weapon_exist(self, weapon_name):
        weaponlist = ["sarastro", "illuminare", "metis"]
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

    @commands.command()
    async def weapon(self, ctx: commands.Context, *args) -> None:
        if len(args) > 1:
            weapon_name = args[0] + " " + args[1]
        else:
            weapon_name = args[0]
        
        match weapon_name:
            # case "lumi":
            #     weapon_name = "luminance"
            # case "evil liv" | "seggs" | "green jumper":
            #     weapon_name = "lux"
            # case "empy" | "solaeter":
            #     weapon_name = "empyrea"
            case "daren" | "scire":
                weapon_name = "illuminare"
            case "capri" | "crapi" | "schizo" | "capriccio":
                weapon_name = "sarastro"
            # case "uncle" | "king engine" | "kingengine" | "wata":
            #     weapon_name = "epitaph"
            # case "supercar" | "hyper":
            #     weapon_name = "hyperreal"
            # case "cow":
            #     weapon_name = "kaleido"
            case "lullaby" | "lost lullaby" | "fish" | "lamia":
                weapon_name = "metis"
            # case "weave" | "motivation" | "vergil's daughter":
            #     weapon_name = "crimson weave"
            # case "awoo" | "furry":
            #     weapon_name = "feral"
            # case "indomitus":
            #     weapon_name = "noctis"
            case _:
                weapon_name = weapon_name            

        print(weapon_name)
        if(self.does_weapon_exist(weapon_name)):
            print(weapon_name)
            weapon = self.retrieve_weapon(weapon_name)
            embed = self.embedconf.create_weapon_embed(weapon)
            await ctx.send(embed=embed)
        else:
            content = "This weapon does not exist. Please try again."
            await ctx.send(content=content)


async def setup(bot: commands.Bot):
    await bot.add_cog(Weapons(bot))

async def teardown(bot):
    print("Extension unloaded!")
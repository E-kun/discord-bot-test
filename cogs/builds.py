
from __future__ import annotations

import typing
import traceback
import discord
import os
import json
from discord.ext import commands
from discord.ext.commands import BucketType, cog, BadArgument, command, cooldown
from utility.embedconfig import EmbedClass
from utility.build_dropdown import DropdownView
from utility.nickname_checker import check_nickname

from discord.ui.select import BaseSelect

class Builds(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()

    def retrieve_build(self, character):
        with open('data/builds.json') as file:
            parsed_json = json.load(file)
        return parsed_json[character]

    def does_character_exist(self, character):
        framelist = ["lotus", "eclipse", "storm", "dawn", "lux", "palefire", "nightblade", "zero", "blast", "luminance", "entropy","ember", "pulse", "tenebrion","crimson abyss", "bastion", "astral", "brilliance", "veritas", "sophia", "arclight", "plume", "rozen", "camu", "rosetta", "changyu", "pavo", "laurel","2b", "9s", "a2", "hypnos", "tempest", "glory", "xxi", "garnet", "roland", "empyrea", "capriccio", "pulao", "starfarer", "haicma", "scire", "noan", "bambinata", "balter", "kaleido", "hyperreal", "crimson weave", "zitherwoe", "feral", "noctis", "alisa", "lamia", "brs", "epitaph"]
        exists = False

        for i in framelist:
            if character == i:
                exists = True
                break
            else:
                exists = False

        return exists

    @commands.Cog.listener()
    async def on_ready(self):
        print('Builds loaded.')

    @commands.command()
    async def buildnotation(self, ctx: commands.Context):
        embed = discord.Embed(title="",description="")
        embed.set_image(url="https://media.discordapp.net/attachments/1272207225800228958/1276390658126512128/PGR_Rank_Terminology.png?ex=66c95aef&is=66c8096f&hm=dac5f98c2a9052a7634f8588155ae68c79073cb04c3a4ec44f150db6548e9827&=&format=webp&quality=lossless&width=550&height=331")
        await ctx.send(embed=embed)

    @commands.command()
    async def build(self, ctx: commands.Context, *args) -> None:
        if len(args) > 1:
            character = args[0] + " " + args[1]
        else:
            character = args[0]
        
        character = check_nickname(character, "character")   

        print(character)

        if(self.does_character_exist(character)):
            build = self.retrieve_build(character)
            data = build['set_list']
            view = DropdownView(ctx.author, data=data, build=build)
            embed = self.embedconf.create_build_embed(build, data[0])
            await ctx.send(view=view, embed=embed)
        else:
            content = "This character does not exist. Please try again."
            await ctx.send(content=content)
    
        
async def setup(bot: commands.Bot):
    await bot.add_cog(Builds(bot))

async def teardown(bot):
    print("Extension unloaded!")
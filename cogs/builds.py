
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

    def retrieve_characterlist(self):
        with open('data/characterlist.json') as file:
            parsed_json = json.load(file)
        return parsed_json['characterlist']

    def does_character_exist(self, character):
        framelist = self.retrieve_characterlist()
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
        embed.set_image(url='https://pgr-discord-bot.s3.ap-southeast-2.amazonaws.com/cnnotationguide4.png')
        await ctx.send(embed=embed)

    @commands.command()
    async def build(self, ctx: commands.Context, *args) -> None:
        character = ""
        if len(args) > 1:
            for idx, arg in enumerate(args):
                if(idx) == 0:
                    character =  character + args[idx]
                else:
                    character =  character + " " + args[idx]
        else:
            character = args[0]
        
        character = check_nickname(character, "character")   

        print(character)

        if(self.does_character_exist(character)):
            build = self.retrieve_build(character)
            data = build['set_list']
            view = DropdownView(ctx.author, data=data, build=build)
            embed = self.embedconf.create_build_embed(build, data[0])
            if len(data) == 1:
                await ctx.send(embed=embed)
            else:
                await ctx.send(view=view, embed=embed)
        else:
            content = "This character does not exist. Please try again."
            await ctx.send(content=content)
    
        
async def setup(bot: commands.Bot):
    await bot.add_cog(Builds(bot))

async def teardown(bot):
    print("Extension unloaded!")

from __future__ import annotations

import typing
import traceback
import discord
import os
import json
from discord.ext import commands
from discord.ext.commands import BucketType, cog, BadArgument, command, cooldown
from embedconfig import EmbedClass
from build_dropdown import DropdownView

from discord.ui.select import BaseSelect

class Builds(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()

    def retrieve_build(self, character):
        with open('data/builds.json') as file:
            parsed_json = json.load(file)
        
        match character:
            case "daren" | "bonka" | "tsundere":
                character = "scire"
            case "capri" | "crapi" | "schizo" | "cappuccino" | "soup":
                character = "capriccio"
            case _:
                character = character

        return parsed_json[character]

    @commands.Cog.listener()
    async def on_ready(self):
        print('Builds loaded.')

    @commands.command()
    async def build(self, ctx: commands.Context, character) -> None:
        build = self.retrieve_build(character)
        # data = ["String 1", "String 2", "String 3"]
        data = build['set_list']
        view = DropdownView(ctx.author, data=data, build=build)
        # content=""
        # string = "String 1"
        # embed = discord.Embed(title=f"{string}",description=f"Description of {string}")
        embed = self.embedconf.create_build_embed(build, data[0])
        await ctx.send(view=view, embed=embed)
        
async def setup(bot: commands.Bot):
    await bot.add_cog(Builds(bot))

async def teardown(bot):
    print("Extension unloaded!")
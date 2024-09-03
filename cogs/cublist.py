from __future__ import annotations

import typing
import traceback
import discord
import os
import json
from discord.ext import commands
from discord.ext.commands import BucketType, cog, BadArgument, command, cooldown
from utility.embedconfig import EmbedClass
from utility.pagination import PaginationView

from discord.ui.select import BaseSelect

class CUBList(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()

    def retrieve_cublist(self):
        with open('data/cublist.json') as file:
            parsed_json = json.load(file)
        return parsed_json['cublist_categorized']

    @commands.Cog.listener()
    async def on_ready(self):
        print('CUBList loaded.')

    @commands.command()
    async def cublist(self, ctx: commands.Context) -> None:
        cubs = self.retrieve_cublist()
        embed = self.embedconf.create_cublist_embed(cubs=cubs)
        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(CUBList(bot))

async def teardown(bot):
    print("Extension unloaded!")
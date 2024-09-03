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

class MemoryList(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()

    def retrieve_memorylist(self):
        with open('data/memorylist.json') as file:
            parsed_json = json.load(file)
        return parsed_json['memories']

    @commands.Cog.listener()
    async def on_ready(self):
        print('MemoryList loaded.')

    @commands.command()
    async def memorylist(self, ctx: commands.Context) -> None:
        list = self.retrieve_memorylist()

        embed = self.embedconf.create_list_embed(list, "memories")
        await ctx.send(embed=embed)
        
async def setup(bot: commands.Bot):
    await bot.add_cog(MemoryList(bot))

async def teardown(bot):
    print("Extension unloaded!")
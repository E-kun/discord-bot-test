
from __future__ import annotations

import typing
import traceback
import discord
import os
from discord.ext import commands
from discord.ext.commands import BucketType, cog, BadArgument, command, cooldown
from embedconfig import EmbedClass
from pagination import PaginationView

from discord.ui.select import BaseSelect

class MemoryList(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print('MemoryList loaded.')

    @commands.command()
    async def memorylist(self, ctx: commands.Context) -> None:
        # print(dir(ctx))
        data = range(1,15)
        testview = PaginationView(ctx.author)
        # await ctx.send("Testing", view=testview)
        # print(dir(view))
        testview.message = await ctx.send("Testing", view=testview)
        # print(testview.message)
        


async def setup(bot: commands.Bot):
    await bot.add_cog(MemoryList(bot))

async def teardown(bot):
    print("Extension unloaded!")
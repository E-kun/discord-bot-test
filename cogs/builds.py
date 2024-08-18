
from __future__ import annotations

import typing
import traceback
import discord
import os
from discord.ext import commands
from discord.ext.commands import BucketType, cog, BadArgument, command, cooldown
from embedconfig import EmbedClass
from dropdown import DropdownView

from discord.ui.select import BaseSelect

class Builds(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print('Builds loaded.')

    @commands.command()
    async def build(self, ctx: commands.Context) -> None:
        # print(dir(ctx))
        # data = range(1,15)
        view = DropdownView(ctx.author)
        # await ctx.send("Testing", view=testview)
        # print(dir(view))
        view.message = await ctx.send("Testing", view=view)
        # print(testview.message)
        


async def setup(bot: commands.Bot):
    await bot.add_cog(Builds(bot))
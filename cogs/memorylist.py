from __future__ import annotations

import typing
import traceback
import discord
import os
import json
from discord.ext import commands
from discord.ext.commands import BucketType, cog, BadArgument, command, cooldown
from embedconfig import EmbedClass
from pagination import PaginationView

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
        # print(dir(ctx))
        # data = range(1,15)
        # testview = PaginationView(ctx.author)
        # await ctx.send("Testing", view=testview)
        # print(dir(view))
        # testview.message = await ctx.send("Testing", view=testview)
        # print(testview.message)
        # if(self.does_character_exist(character)):
        list = self.retrieve_memorylist()
        # view = DropdownView(ctx.author, data=data, build=build)
        embed = self.embedconf.create_list_embed(list, "memories")
        await ctx.send(embed=embed)
        # else:
        #     content = "This character does not exist. Please try again."
        #     await ctx.send(content=content)
        


async def setup(bot: commands.Bot):
    await bot.add_cog(MemoryList(bot))

async def teardown(bot):
    print("Extension unloaded!")
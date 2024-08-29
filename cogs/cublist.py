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

class CubList(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()

    def retrieve_weaponlist(self):
        with open('data/weaponlist.json') as file:
            parsed_json = json.load(file)
        return parsed_json['weaponlist']

    @commands.Cog.listener()
    async def on_ready(self):
        print('WeaponList loaded.')

    @commands.command()
    async def cublist(self, ctx: commands.Context) -> None:
        # print(dir(ctx))
        # data = range(1,15)
        # testview = PaginationView(ctx.author)
        # await ctx.send("Testing", view=testview)
        # print(dir(view))
        # testview.message = await ctx.send("Testing", view=testview)
        # print(testview.message)
        # if(self.does_character_exist(character)):
        list = self.retrieve_weaponlist()
        # view = DropdownView(ctx.author, data=data, build=build)
        embed = self.embedconf.create_list_embed(list, "weapons")
        await ctx.send(embed=embed)
        # else:
        #     content = "This character does not exist. Please try again."
        #     await ctx.send(content=content)
        


async def setup(bot: commands.Bot):
    await bot.add_cog(CubList(bot))

async def teardown(bot):
    print("Extension unloaded!")
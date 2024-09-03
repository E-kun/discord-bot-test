from __future__ import annotations

import typing
import traceback
import discord
import os
import json
from discord.ext import commands
from discord.ext.commands import BucketType, cog, BadArgument, command, cooldown
from utility.embedconfig import EmbedClass
from utility.weplist_pagination import WeaponListPaginationView

from discord.ui.select import BaseSelect

class WeaponList(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()

    def retrieve_weaponlist(self):
        with open('data/weaponlist.json') as file:
            parsed_json = json.load(file)
        return parsed_json['weaponlist_categorised']

    @commands.Cog.listener()
    async def on_ready(self):
        print('WeaponList loaded.')

    @commands.command()
    async def weaponlist(self, ctx: commands.Context) -> None:
        categories = self.retrieve_weaponlist()
        weplistview = WeaponListPaginationView(ctx.author, data=categories)

        embed = self.embedconf.create_list_embed(name=categories[0]['name'], items=categories[0]['list'], curpage=1, maxlistcount=len(categories))
        await ctx.send(embed=embed, view=weplistview)

async def setup(bot: commands.Bot):
    await bot.add_cog(WeaponList(bot))

async def teardown(bot):
    print("Extension unloaded!")
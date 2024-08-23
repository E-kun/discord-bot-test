import discord
import os
from discord.ext import commands
from discord.ext.commands import BucketType, cog, BadArgument, command, cooldown
from embedconfig import EmbedClass

class About(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()

    @commands.Cog.listener()
    async def on_ready(self):
        print('About loaded.')

    @commands.command()
    async def about(self, ctx: commands.Context):
        embed = self.embedconf.create_about_embed()
        await ctx.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(About(bot))

async def teardown(bot):
    print("Extension unloaded!")
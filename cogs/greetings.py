import discord
import os
from discord.ext import commands
from discord.ext.commands import BucketType, cog, BadArgument, command, cooldown
from utility.embedconfig import EmbedClass
from utility.pagination import PaginationView

class TestCog(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('TestCog loaded.')

    @commands.command()
    async def test(self, ctx):
        message = "I'm alive"
        title = "Test Message"
        embed = EmbedClass(message, title)
        await ctx.channel.send(embed=embed.embed)

    @commands.command()
    async def ping(self, ctx):
        message = f'⏱|** {round(self.bot.latency * 1000)} ms** Latency!'
        title = "Ping"
        embed = EmbedClass(message, title)
        await ctx.send(embed=embed.embed)

    @commands.command()
    async def paginate(self, ctx: commands.Context) -> None:
        view = PaginationView(ctx.author)
        # print(view.children)
        embed = discord.Embed(title="Pagination Test", description="Pagination Test")
        await ctx.send(view=view, embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(TestCog(bot))

async def teardown(bot):
    print("Extension unloaded!")
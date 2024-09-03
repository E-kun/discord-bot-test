import discord
import os
from discord.ext import commands
from discord.ext.commands import BucketType, cog, BadArgument, command, cooldown
from utility.embedconfig import EmbedClass

class Help(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Help loaded.')

    @commands.command()
    async def help(self, ctx):
        commands = ["**?build**", "**?weapon/wep/weap/sig**", "**?basic, red, yellow, blue, core, signature/ult, leader, qte, class, ss, sss, s+**", "**?cub/pet**", "**?time/ppc**", "**?help**", "**?about**", "**?weaponlist**", "**?cublist**"]
        # content="List of commands"
        embed = discord.Embed(
            title=f"Celica Bot Command List",
            description=f""
        )
        for i in commands:
            embed.add_field(
                name="",
                value=f"{i}",
                inline=False
            )

        await ctx.channel.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Help(bot))

async def teardown(bot):
    print("Extension unloaded!")
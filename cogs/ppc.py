import discord
import os
from discord.ext import commands
from discord.ext.commands import BucketType, cog, BadArgument, command, cooldown
from embedconfig import EmbedClass

class Ppc(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('PPC loaded.')

    @commands.command(pass_context=True)
    async def time(self, ctx, difficulty, time):
        maxSeconds = 300
        match difficulty:
            case "test":
                maxScore = 21000
                minScore = 9750
                increment = 2
            case "elite":
                maxScore = 42000
                minScore = 19500
                increment = 2
            case "knight":
                maxScore = 84000
                minScore = 39000
                increment = 2
            case "chaos":
                maxScore = 168000
                minScore = 78000
                increment = 2
                # scorePerSecond = 
            case "hell":
                maxScore = 336000
                minScore = 156000
                increment = 4
                scorePerSecond = 600
            case _:
                maxScore = "%s is not a valid difficulty!" % (difficulty)
                # defaultTitle = ""
        

        intTime = int(time)
        if(intTime >= maxSeconds):
            timeScore = 0
        else:
            timeScore = (scorePerSecond - (increment*int(time)))*(maxSeconds-int(time))
        
        score = minScore + timeScore

        message = score
        title = "%s max score" % (difficulty.title())  
        embed = EmbedClass(message, title)
        await ctx.channel.send(embed=embed.embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Ppc(bot))

async def teardown(bot):
    print("Extension unloaded!")
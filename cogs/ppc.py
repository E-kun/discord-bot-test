import discord
import os
from discord.ext import commands
from discord.ext.commands import BucketType, cog, BadArgument, command, cooldown
from utility.embedconfig import EmbedClass

class Ppc(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def check_difficulty(self, difficulty):
        difflist = ["test", "elite", "knight", "chaos", "hell"]
        exists = False

        for i in difflist:
            if difficulty == i:
                exists = True
                break
            else:
                exists = False

        return exists

    @commands.Cog.listener()
    async def on_ready(self):
        print('PPC loaded.')

    @commands.command(pass_context=True, aliases=["ppc"])
    async def time(self, ctx, difficulty, time):
        maxSeconds = 300
        difficulties = ["test", "elite", "knight", "chaos", "hell"]
        match difficulty:
            case "test":
                power = 0
                maxScore = 21000
                minScore = 9750
            case "elite":
                power = 1
                maxScore = 42000
                minScore = 19500
            case "knight":
                power = 2
                maxScore = 84000
                minScore = 39000
            case "chaos":
                power = 3
                maxScore = 168000
                minScore = 78000
            case "hell":
                power = 4
                maxScore = 336000
                minScore = 156000
            case _:
                maxScore = "%s is not a valid difficulty!" % (difficulty)
        
        try:
            intTime = abs(int(time))
        except:
            content = f"The provided time needs to be a number between 0 seconds and 300 seconds(5 mins)!"
            await ctx.channel.send(content=content)
        
        if(self.check_difficulty(difficulty)):
            if(intTime >= maxSeconds):
                minutes = 5
                seconds = "00"
                intScore = minScore
                embed = discord.Embed(
                    title="",
                    description=f"**{difficulty.title()} {minutes}:{seconds}**"
                )
                embed.add_field(name="", value=f"Final Score: {intScore}", inline=False)
                embed.add_field(name="", value=f"# You must have some skill issue if you even considered going over 5 minutes for EXPPC. :upside_down:", inline=False)
                await ctx.channel.send(embed=embed)
            else:
                minutes = 0
                if intTime > 60:
                    minutes = intTime//60
                    seconds = intTime%60
                    if seconds < 10:
                        seconds = f"0{seconds}"
                else:
                    minutes = 0
                    seconds = intTime
                    if seconds < 10:
                        seconds = f"0{seconds}"

                factor = 2**power
                timeplusone = intTime+1
                score = 21000 * factor - round((74.875 * float(factor) * float(timeplusone)) - (0.25 * float(factor) * float(timeplusone) * (float(timeplusone)-1.0) / 2.0), 0)

                intScore = int(score)

                title = "%s max score" % (difficulty.title())  
                embed = discord.Embed(
                    title="",
                    description=f"**{difficulty.title()} {minutes}:{seconds}**"
                )
                embed.add_field(name="", value=f"Final Score: {intScore}", inline=False)
                await ctx.channel.send(embed=embed)
        else:
            content = f"{difficulty} is not a valid difficulty!"
            await ctx.channel.send(content=content)

async def setup(bot: commands.Bot):
    await bot.add_cog(Ppc(bot))

async def teardown(bot):
    print("Extension unloaded!")
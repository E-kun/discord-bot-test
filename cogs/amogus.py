import discord
import os
from random import randrange
from discord.ext import commands
from discord.ext.commands import BucketType, cog, BadArgument, command, cooldown
from utility.embedconfig import EmbedClass
import json

class Amogus(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def read_file(self, filename):
        with open('data/pgr_graph.json') as file:
            parsed_json = json.load(file)
        return parsed_json['graph']

    @commands.Cog.listener()
    async def on_ready(self):
        print('Amogus loaded.')


    @commands.command()
    async def miku(self, ctx, *args):
        graphs = self.read_file('data/pgr_graph.json')

        if len(args) == 0:
            embed = discord.Embed(
            title=f"Miku",
            description=f"Hi this is Miku nya! I'm here today to give you valuable information nya!",
            # color=discord.colour(value=0xfc5f21)
            )
        else:

            match args[0]:
                case "alpha" | "ca" | "abyss":
                    graph_url = "Crimson_Abyss"
                case "lumi" :
                    graph_url = "Liv_Luminance"
                case "dawn":
                    graph_url = "Lucia_Dawn"
                case "daren" | "scire":
                    graph_url = "Karenina_Scire"
                case "brsvshyper":
                    graph_url = "BRSvsHyperreal"
                case "wanshi":
                    graph_url = "Wanshi_Lucid"
                case "lamia":
                    graph_url = "Lamia"
                case "weave" | "cw":
                    graph_url = "Crimson_Weave"
                case "feral" | "woof":
                    graph_url = "No21_Feral"
                case "alisa":
                    graph_url = "Alisa_Echo"
                case "lumivecho":
                    graph_url = "LumivsEcho"
                case _:
                    graph_url = graph_url

            embed = discord.Embed(
            title=f"Miku",
            description=f"Hi this is Miku nya! I'm here today to give you valuable information nya!",
            # color=discord.colour(value=0xfc5f21)
            )
            embed.set_image(url=graphs[graph_url])
        
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def pasta(self, ctx):
        embed = discord.Embed(
            title="",
            description=f"This is a random copypasta",
            # color=discord.colour(value=0xfc5f21)
        )
        await ctx.channel.send(embed=embed)
    
    @commands.command()
    async def lewd(self, ctx):
        # content=f"<:livwhat:1272193716425195543>"
        embed = discord.Embed(
            title="",
            description=f"<:livwhat:1272193716425195543>",
            # color=discord.colour(value=0xfc5f21)
        )
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def brick(self, ctx):
        embed = discord.Embed(
            title="",
            description=f"🧱",
            # color=discord.colour(value=0xfc5f21)
        )
        await ctx.channel.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Amogus(bot))

async def teardown(bot):
    print("Extension unloaded!")
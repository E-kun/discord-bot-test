import discord
import os
import json
from discord.ext import commands
from discord.ext.commands import BucketType, cog, BadArgument, command, cooldown
from utility.embedconfig import EmbedClass
from utility.nickname_checker import check_nickname

class CUBs(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()

    def retrieve_cub(self, cub):
        with open('data/cubs.json') as file:
            parsed_json = json.load(file)
        return parsed_json[cub]

    def does_cub_exist(self, cub_name):
        cublist = ["cetus", "seeshell", "thorny", "yuan ye", "lingya", "dawn chorus", "toniris", "jet jaeger", "frost oath", "nitor", "motorbolt", "punchy", "moonhopper", "hades fangs", "rainbow", "noctua", "boreas", "shimmer"]
        exists = False

        for i in cublist:
            if cub_name == i:
                exists = True
                break
            else:
                exists = False

        return exists

    @commands.Cog.listener()
    async def on_ready(self):
        print('CUBs loaded.')

    @commands.command(aliases=["pet"])
    async def cub(self, ctx: commands.Context, *args) -> None:
        cub_name = ""
        if len(args) > 1:
            for idx, arg in enumerate(args):
                if(idx) == 0:
                    cub_name =  cub_name + args[idx]
                else:
                    cub_name =  cub_name + " " + args[idx]
        else:
            cub_name = args[0]
        
        cub_name = check_nickname(cub_name, "cub")           

        print(cub_name)
        if(self.does_cub_exist(cub_name)):
            print(cub_name)
            cub = self.retrieve_cub(cub_name)
            embed = self.embedconf.create_cub_embed(cub)
            await ctx.send(embed=embed)
        else:
            content = "This CUB does not exist. Please try again."
            await ctx.send(content=content)


async def setup(bot: commands.Bot):
    await bot.add_cog(CUBs(bot))

async def teardown(bot):
    print("Extension unloaded!")
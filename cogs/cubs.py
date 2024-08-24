import discord
import os
import json
from discord.ext import commands
from discord.ext.commands import BucketType, cog, BadArgument, command, cooldown
from utility.embedconfig import EmbedClass

class CUBs(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()

    def retrieve_cub(self, cub):
        with open('data/cubs.json') as file:
            parsed_json = json.load(file)
        return parsed_json[cub]

    def does_cub_exist(self, cub_name):
        cublist = ["cetus"]
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
        if len(args) > 1:
            cub_name = args[0] + " " + args[1]
        else:
            cub_name = args[0]
        
        match cub_name:
            # case "lumi":
            #     weapon_name = "luminance"
            # case "evil liv" | "seggs" | "green jumper":
            #     weapon_name = "lux"
            # case "empy" | "solaeter":
            #     weapon_name = "empyrea"
            # case "daren" | "scire":
            #     cub_name = "boone"
            # case "capri" | "crapi" | "schizo" | "capriccio":
            #     cub_name = "seraphine"
            # case "uncle" | "king engine" | "kingengine" | "wata":
            #     weapon_name = "epitaph"
            # case "supercar" | "hyper":
            #     weapon_name = "hyperreal"
            # case "cow":
            #     weapon_name = "kaleido"
            case "lullaby" | "lost lullaby" | "fish" | "lamia":
                cub_name = "cetus"
            # case "weave" | "motivation" | "vergil's daughter":
            #     weapon_name = "crimson weave"
            # case "awoo" | "furry":
            #     weapon_name = "feral"
            # case "indomitus":
            #     weapon_name = "noctis"
            case _:
                cub_name = cub_name            

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
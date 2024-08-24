import discord
import os
import json
from discord.ext import commands
from discord.ext.commands import BucketType, cog, BadArgument, command, cooldown
from utility.embedconfig import EmbedClass

class Memories(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()

    def retrieve_memory(self, memory):
        with open('data/mems.json') as file:
            parsed_json = json.load(file)
        return parsed_json[memory]

    def does_memory_exist(self, memory_name):
        memorylist = ["cottie", "edison", "aife", "ike", "einsteina", "archimedes", "alice", "patton", "bianca: tipsy night", "isabel", "kuriko eternal", "boone", "darwin", "da vinci", "derketo", "diesel", "lucia - summer daze", "seraphine", "philip", "frederick", "voltaire", "condelina", "shakespeare", "heisen", "hanna", "catherine", "guinevere", "bathlon", "chen jiyuan", "leeuwenhoek", "flamel", "tifa", "elizabeth", "unimate", "charlotte", "turing", "aline", "fran", "signa", "alphonse"]
        exists = False

        for i in memorylist:
            if memory_name == i:
                exists = True
                break
            else:
                exists = False

        return exists

    @commands.Cog.listener()
    async def on_ready(self):
        print('Memory loaded.')

    @commands.command()
    async def memory(self, ctx: commands.Context, *args) -> None:
        if len(args) > 1:
            memory_name = args[0] + " " + args[1]
        else:
            memory_name = args[0]
        
        match memory_name:
            # case "lumi":
            #     weapon_name = "luminance"
            # case "evil liv" | "seggs" | "green jumper":
            #     weapon_name = "lux"
            # case "empy" | "solaeter":
            #     weapon_name = "empyrea"
            # case "daren" | "scire":
            #     memory_name = "boone"
            # case "capri" | "crapi" | "schizo" | "capriccio":
            #     memory_name = "seraphine"
            # case "uncle" | "king engine" | "kingengine" | "wata":
            #     weapon_name = "epitaph"
            # case "supercar" | "hyper":
            #     weapon_name = "hyperreal"
            # case "cow":
            #     weapon_name = "kaleido"
            case "lullaby" | "lost lullaby" | "fish" | "lamia":
                memory_name = "derketo"
            # case "weave" | "motivation" | "vergil's daughter":
            #     weapon_name = "crimson weave"
            # case "awoo" | "furry":
            #     weapon_name = "feral"
            # case "indomitus":
            #     weapon_name = "noctis"
            case _:
                memory_name = memory_name            

        print(memory_name)
        if(self.does_memory_exist(memory_name)):
            print(memory_name)
            memory = self.retrieve_memory(memory_name)
            embed = self.embedconf.create_memory_embed(memory)
            await ctx.send(embed=embed)
        else:
            content = "This memory does not exist. Please try again."
            await ctx.send(content=content)


async def setup(bot: commands.Bot):
    await bot.add_cog(Memories(bot))

async def teardown(bot):
    print("Extension unloaded!")
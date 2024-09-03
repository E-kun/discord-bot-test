import discord
import os
import json
from discord.ext import commands
from discord.ext.commands import BucketType, cog, BadArgument, command, cooldown
from utility.embedconfig import EmbedClass
from utility.nickname_checker import check_nickname, abbreviation_checker

class Memories(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()

    def retrieve_memory(self, memory):
        with open('data/mems.json') as file:
            parsed_json = json.load(file)
        return parsed_json[memory]

    def does_memory_exist(self, memory_name):
        with open('data/memorylist.json') as file:
            parsed_json = json.load(file)

        memorylist = parsed_json['memorylist']
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

    @commands.command(aliases=["mem", "memo"])
    async def memory(self, ctx: commands.Context, *args) -> None:
        memory_name = ""
        if len(args) > 1:
            for idx, arg in enumerate(args):
                if(idx) == 0:
                    memory_name =  memory_name + args[idx]
                else:
                    memory_name =  memory_name + " " + args[idx]
        else:
            memory_name = args[0]
        
        print(memory_name)
        
        if(self.does_memory_exist(memory_name)):
            memory = self.retrieve_memory(memory_name)
            embed = self.embedconf.create_memory_embed(memory)
            await ctx.send(embed=embed)
        elif(abbreviation_checker(memory_name) != "n/a"):
            memory = abbreviation_checker(memory_name)
            if(self.does_memory_exist(memory)):
                memory = self.retrieve_memory(memory)
                embed = self.embedconf.create_memory_embed(memory)
                await ctx.send(embed=embed)
            else:
                content = "This memory does not exist. Please try again."
                await ctx.send(content=content)
        else:
            memory_name = check_nickname(memory_name, "memory")            
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
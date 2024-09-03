import discord
import os
import json
from discord.ext import commands
from discord.ext.commands import BucketType, cog, BadArgument, command, cooldown
from utility.embedconfig import EmbedClass
from utility.nickname_checker import abbreviation_checker, check_nickname

class Minmax(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()

    @commands.Cog.listener()
    async def on_ready(self):
        print('Minmax loaded.')
    
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

    def memory_checker(self, memory_name):
        if(self.does_memory_exist(memory_name)):
            memory = self.retrieve_memory(memory_name)
            return memory
        elif(abbreviation_checker(memory_name) != "n/a"):
            memory = abbreviation_checker(memory_name)
            if(self.does_memory_exist(memory)):
                memory = self.retrieve_memory(memory)
                return memory
            else:
                memory = {}
                return memory
        else:
            memory_name = check_nickname(memory_name, "memory")            

            if(self.does_memory_exist(memory_name)):
                # print(memory_name)
                memory = self.retrieve_memory(memory_name)
                return memory
            else:
                memory = {}
                return memory
                

    @commands.command()
    async def minmax(self, ctx: commands.Context, *args):
        focus = ""
        compare_with = ""
        first_argument = True
        word_count = 0
        
        if(not args == ()):
            if(len(args)== 1):
                if("," not in args[0]):
                    await ctx.send("There is only one argument here! You need to provide 2 memories separated by a comma.")
                else:
                    focus = args[0].split(",")[0]
                    compare_with = args[0].split(",")[1]
        
            elif(len(args) > 1):
                for idx,i in enumerate(args):
                    if(first_argument):
                        
                        if(word_count == 0):
                            focus = i
                        else:
                            focus = focus + " " + i
                        if("," in i):
                            first_argument = False
                            word_count = 0
                        word_count+=1
                    else:
                        if(word_count == 0):
                            compare_with = i
                        else:
                            compare_with = compare_with + " " + i
                        word_count += 1

                print(focus.split(",")[0])
                print(compare_with.strip())
                        
                focus = focus.split(",")[0]
                compare_with = compare_with.strip()

            focus_memory = self.memory_checker(focus)
            compare_with_memory = self.memory_checker(compare_with)

            if(focus_memory == {} or compare_with_memory == {}):
                await ctx.send(content="Either one of these memories are not valid! Please enter 2 valid memories to be compared.")
            else:
                if(focus_memory['atk'] > compare_with_memory['atk']):
                    top_mem = compare_with_memory
                    bot_mem = focus_memory
                else:
                    top_mem = focus_memory
                    bot_mem = compare_with_memory

                embed = discord.Embed(
                    title="Minmax",
                    description="",
                    color=discord.Color(value=0xc3d8fa)
                )

                embed.add_field(
                    name=f"{top_mem['name']} goes Top", 
                    value=f"""
                        `ATK  : {top_mem['atk']}   `
                        `DEF  : {top_mem['def']}   `
                        `CRIT : {top_mem['crit']}    `
                        `HP   : {top_mem['hp']}  `
                        """)
                
                embed.add_field(
                    name=f"{bot_mem['name']} goes Bottom", 
                    value=f"""
                        `ATK : {bot_mem['atk']}   `
                        `DEF : {bot_mem['def']}   `
                        `CRIT: {bot_mem['crit']}    `
                        `HP  : {bot_mem['hp']}  `
                        """)

                await ctx.send(embed=embed)
            
        else:
            content = f"There are no memories to compare! Please include 2 memories separated by a comma."
            await ctx.channel.send(content=content)

async def setup(bot: commands.Bot):
    await bot.add_cog(Minmax(bot))

async def teardown(bot):
    print("Extension unloaded!")
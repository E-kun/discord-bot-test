
from __future__ import annotations

import typing
import traceback
import discord
import os
import json
from discord.ext import commands
from discord.ext.commands import BucketType, cog, BadArgument, command, cooldown
from utility.embedconfig import EmbedClass
from utility.build_dropdown import DropdownView
from utility.nickname_checker import check_nickname
from utility.core_pagination import CorePaginationView

from discord.ui.select import BaseSelect

class Skills(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()

    def retrieve_skills(self, character):
        with open('data/skills.json') as file:
            parsed_json = json.load(file)
        return parsed_json[character]

    def does_character_exist(self, character):
        with open('data/characterlist.json') as file:
            parsed_json = json.load(file)
        framelist = parsed_json['characterlist']
        exists = False

        for i in framelist:
            if character == i:
                exists = True
                break
            else:
                exists = False

        return exists

    async def grab_skill(self, ctx, character, skill_type):
        if(self.does_character_exist(character)):
            skillset = self.retrieve_skills(character)
            match skill_type:
                case 'basic':
                    skill = skillset['basic_attack']
                    skill_type = 'basic'
                case 'red':
                    skill = skillset['red_orb']
                    skill_type = 'red'
                case 'yellow':
                    skill = skillset['yellow_orb']
                    skill_type = 'yellow'
                case 'blue':
                    skill = skillset['blue_orb']
                    skill_type = 'blue'
                case 'core':
                    skill = skillset['core_passive']
                    skill_type = 'core'
                case 'signature':
                    skill = skillset['signature']
                    skill_type = 'signature'
                case 'qte':
                    skill = skillset['qte']
                    skill_type = 'qte'
                case 'leader':
                    skill = skillset['leader']
                    skill_type = 'leader'
                case 'class':
                    skill = skillset['class']
                    skill_type = 'class'
                case 'ss':
                    skill = skillset['ss_rank']
                    skill_type = 'ss'
                case 'sss':
                    skill = skillset['sss_rank']
                    skill_type = 'sss'
                case 's+':
                    skill = skillset['s+_rank']
                    skill_type = 's+'
            
            # data = build['set_list']
            # view = DropdownView(ctx.author, data=data, build=build)
            if skill_type == 'core':
                # print(skill)
                embed = self.embedconf.create_corepassive_embed(skill, 0)
                corepageview = CorePaginationView(ctx.author, data=skill)
                await ctx.send(embed=embed, view=corepageview)
            else:
                embed = self.embedconf.create_skills_embed(skill, skill_type)
                await ctx.send(embed=embed)
        else:
            content = "This character does not exist. Please try again."
            await ctx.send(content=content)


    @commands.Cog.listener()
    async def on_ready(self):
        print('Skills loaded.')

    @commands.command()
    async def basic(self, ctx: commands.Context, *args) -> None:
        if len(args) > 1:
            character = args[0] + " " + args[1]
        else:
            character = args[0]
        
        print(character)

        character = check_nickname(character, "character")

        print(character)

        await self.grab_skill(ctx, character, 'basic')
    
    @commands.command()
    async def red(self, ctx: commands.Context, *args) -> None:
        if len(args) > 1:
            character = args[0] + " " + args[1]
        else:
            character = args[0]

        print(character)
        
        character = check_nickname(character, "character")

        print(character)

        await self.grab_skill(ctx, character, 'red')
    
    @commands.command()
    async def yellow(self, ctx: commands.Context, *args) -> None:
        if len(args) > 1:
            character = args[0] + " " + args[1]
        else:
            character = args[0]

        print(character)
        
        character = check_nickname(character, "character")

        print(character)

        await self.grab_skill(ctx, character, 'yellow')

    @commands.command()
    async def blue(self, ctx: commands.Context, *args) -> None:
        if len(args) > 1:
            character = args[0] + " " + args[1]
        else:
            character = args[0]

        print(character)
        
        character = check_nickname(character, "character")

        print(character)

        await self.grab_skill(ctx, character, 'blue')

    @commands.command()
    async def core(self, ctx: commands.Context, *args) -> None:
        if len(args) > 1:
            character = args[0] + " " + args[1]
        else:
            character = args[0]

        print(character)
        
        character = check_nickname(character, "character")

        print(character)

        await self.grab_skill(ctx, character, 'core')
        
    @commands.command(aliases=['ult'])
    async def signature(self, ctx: commands.Context, *args) -> None:
        if len(args) > 1:
            character = args[0] + " " + args[1]
        else:
            character = args[0]

        print(character)
        
        character = check_nickname(character, "character")

        print(character)

        await self.grab_skill(ctx, character, 'signature')

    @commands.command()
    async def qte(self, ctx: commands.Context, *args) -> None:
        if len(args) > 1:
            character = args[0] + " " + args[1]
        else:
            character = args[0]

        print(character)
        
        character = check_nickname(character, "character")

        print(character)

        await self.grab_skill(ctx, character, 'qte')

    @commands.command()
    async def leader(self, ctx: commands.Context, *args) -> None:
        if len(args) > 1:
            character = args[0] + " " + args[1]
        else:
            character = args[0]

        print(character)
        
        character = check_nickname(character, "character")

        print(character)

        await self.grab_skill(ctx, character, 'leader')

    @commands.command(name="class")
    async def class_passive(self, ctx: commands.Context, *args) -> None:
        if len(args) > 1:
            character = args[0] + " " + args[1]
        else:
            character = args[0]

        print(character)
        
        character = check_nickname(character, "character")

        print(character)

        await self.grab_skill(ctx, character, 'class')

    @commands.command()
    async def ss(self, ctx: commands.Context, *args) -> None:
        if len(args) > 1:
            character = args[0] + " " + args[1]
        else:
            character = args[0]

        print(character)
        
        character = check_nickname(character, "character")

        print(character)

        await self.grab_skill(ctx, character, 'ss')

    @commands.command()
    async def sss(self, ctx: commands.Context, *args) -> None:
        if len(args) > 1:
            character = args[0] + " " + args[1]
        else:
            character = args[0]

        print(character)
        
        character = check_nickname(character, "character")

        print(character)

        await self.grab_skill(ctx, character, 'sss')

    @commands.command(name="sss+", aliases=["s+"])
    async def splus(self, ctx: commands.Context, *args) -> None:
        if len(args) > 1:
            character = args[0] + " " + args[1]
        else:
            character = args[0]

        print(character)
        
        character = check_nickname(character, "character")

        print(character)

        await self.grab_skill(ctx, character, 's+')

async def setup(bot: commands.Bot):
    await bot.add_cog(Skills(bot))

async def teardown(bot):
    print("Extension unloaded!")
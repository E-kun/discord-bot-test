
from __future__ import annotations

import typing
import traceback
import discord
import os
import json
from discord.ext import commands
from discord.ext.commands import BucketType, cog, BadArgument, command, cooldown
from embedconfig import EmbedClass
from build_dropdown import DropdownView

from discord.ui.select import BaseSelect

class Builds(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embedconf = EmbedClass()

    def retrieve_build(self, character):
        with open('data/builds.json') as file:
            parsed_json = json.load(file)
        return parsed_json[character]

    def does_character_exist(self, character):
        framelist = ["lotus", "eclipse", "storm", "dawn", "lux", "palefire", "nightblade", "zero", "blast", "luminance", "entropy","ember", "pulse", "tenebrion","crimson abyss", "bastion", "astral", "brilliance", "veritas", "sophia", "arclight", "plume", "rozen", "camu", "rosetta", "changyu", "pavo", "laurel","2b", "9s", "a2", "hypnos", "tempest", "glory", "xxi", "garnet", "roland", "empyrea", "capriccio", "pulao", "starfarer", "haicma", "scire", "noan", "bambinata", "balter", "kaleido", "hyperreal", "crimson weave", "zitherwoe", "feral", "noctis", "alisa", "lamia", "brs", "epitaph"]
        exists = False

        for i in framelist:
            if character == i:
                exists = True
                break
            else:
                exists = False

        return exists

    @commands.Cog.listener()
    async def on_ready(self):
        print('Builds loaded.')

    @commands.command()
    async def build(self, ctx: commands.Context, *args) -> None:
        if len(args) > 1:
            character = args[0] + " " + args[1]
        else:
            character = args[0]

        print(character)
        
        match character:
            case "lumi":
                character = "luminance"
            case "evil liv" | "seggs" | "green jumper" | "<:evilliv:1272415890453041223>":
                character = "lux"
            case "empy" | "solaeter":
                character = "empyrea"
            case "daren" | "bonka" | "tsundere" | "radiant daybreak" | "trs" | "<:trs:1275701510293946482>":
                character = "scire"
            case "capri" | "crapi" | "schizo" | "cappuccino" | "soup" | "pwowq":
                character = "capriccio"
            case "uncle" | "king engine" | "kingengine" | "wata":
                character = "epitaph"
            case "supercar" | "hyper":
                character = "hyperreal"
            case "cow":
                character = "kaleido"
            case "lullaby" | "lost lullaby" | "feesh" | "fish":
                character = "lamia"
            case "weave" | "motivation" | "vergil's daughter":
                character = "crimson weave"
            case "awoo" | "furry":
                character = "feral"
            case "indomitus":
                character = "noctis"
            case _:
                character = character    

        if(self.does_character_exist(character)):
            build = self.retrieve_build(character)
            data = build['set_list']
            view = DropdownView(ctx.author, data=data, build=build)
            embed = self.embedconf.create_build_embed(build, data[0])
            await ctx.send(view=view, embed=embed)
        else:
            content = "This character does not exist. Please try again."
            await ctx.send(content=content)
    
        
async def setup(bot: commands.Bot):
    await bot.add_cog(Builds(bot))

async def teardown(bot):
    print("Extension unloaded!")
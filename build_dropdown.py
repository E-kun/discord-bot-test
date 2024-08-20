from __future__ import annotations

import logging
import discord
import typing
import traceback
import json
from embedconfig import EmbedClass

class DropdownView(discord.ui.View):
    message: discord.Message | None = None
    sep : int = 5
    current_page = 1

    def __init__(self, user: discord.User | discord.Member, timeout: float = 60.0, data = [], build = {}) -> None:
        super().__init__(timeout=timeout)
        self.user = user
        self.data = data
        self.build = build
        self.menu = discord.ui.Select[DropdownView](
            custom_id="persistent_menu",
            placeholder="Select a build",
            min_values=1,
            max_values=1,
            options=[discord.SelectOption(label=f"{i}") for i in data],
        )
        self.menu.callback = self.callback
        self.add_item(self.menu)
        self.embedconf = EmbedClass()

    async def callback(self, interaction: discord.Interaction) -> None:
        # await interaction.response.defer()
        # print(self.menu.values)
        #Call create_embed function when choice has been made to alter the build embed
        # embed = self.choose_text(self.menu.values[0])
        # print(self.build)
        print(self.build)
        # print(self.menu.values[0])
        embed = self.embedconf.create_build_embed(self.build, self.menu.values[0])
        await interaction.response.edit_message(embed=embed, view=self)

    # checks for the view's interactions
    async def interaction_check(self, interaction: discord.Interaction) -> bool:

        if interaction.user == self.user:
            content = "Test"
            # await interaction.response.edit_message(content=content, view=DropdownView)
            return True
        # else send a message and return False
        await interaction.response.send_message(f"The command was initiated by {self.user.mention}", ephemeral=True)
        return False
    
    def choose_text(self, choice):
        string = ""
        str1 = "String 1"
        str2 = "String 2"
        str3 = "String 3"

        match choice:
            case "String 1":
                string = str1
            case "String 2":
                string = str2
            case "String 3":
                string = str3

        embed = discord.Embed(
            title=f'{string}',
            description=f"Description of {string}"
        )

        return embed

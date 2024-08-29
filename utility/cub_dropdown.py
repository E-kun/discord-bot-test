from __future__ import annotations

import logging
import discord
import typing
import traceback
import json
from utility.embedconfig import EmbedClass

class CUBDropdownView(discord.ui.View):

    def __init__(self, user: discord.User | discord.Member, timeout: float = 60.0, cub = {}) -> None:
        super().__init__(timeout=timeout)
        self.user = user
        self.cub = cub
        self.menu = discord.ui.Select[CUBDropdownView](
            custom_id="persistent_menu",
            placeholder="Choose skillset",
            min_values=1,
            max_values=1,
            options=[discord.SelectOption(label=f"Active Skills"), discord.SelectOption(label=f"Passive Skills")],
        )
        self.menu.callback = self.callback
        self.add_item(self.menu)
        self.embedconf = EmbedClass()

    async def callback(self, interaction: discord.Interaction) -> None:
        choice = ""

        if(self.menu.values[0] == "Active Skills"):
            choice = 'active'
        elif(self.menu.values[0] == "Passive Skills"):
            choice = 'passive'

        embed = self.embedconf.create_cub_embed(self.cub, choice)
        await interaction.response.edit_message(embed=embed, view=self)

    # checks for the view's interactions
    async def interaction_check(self, interaction: discord.Interaction) -> bool:

        if interaction.user == self.user:
            content = "Test"
            return True
        # else send a message and return False
        await interaction.response.send_message(f"The command was initiated by {self.user.mention}", ephemeral=True)
        return False
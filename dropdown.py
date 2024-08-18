from __future__ import annotations

import logging
import discord
import typing
import traceback

class DropdownView(discord.ui.View):
    message: discord.Message | None = None
    sep : int = 5
    current_page = 1

    def __init__(self, user: discord.User | discord.Member, timeout: float = 60.0) -> None:
        super().__init__(timeout=timeout)
        self.user = user
        self.data = range(1,15)

    # checks for the view's interactions
    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        
        # view: PaginationView = self.view

        if interaction.user == self.user:
            content = "Test"
            # await self.update_message(self.data[:self.sep])
            # await interaction.response.edit_message(content=content, view=view)
            return True
        # else send a message and return False
        await interaction.response.send_message(f"The command was initiated by {self.user.mention}", ephemeral=True)
        return False
    
    def create_embed(self):
    # def create_embed(self, data):
        embed = discord.Embed(
            title="Lamia: Lost Lullaby",
            description="Awakening Set",
        )
        embed.add_field(name="Usage", value="Main")
        embed.add_field(name="Game Modes", value="Pain Cage, Warzone, Norman, Clash Reflection, High Difficulty")
        embed.add_field(
            name="Description", 
            values="""
            Recommended for all ranks
            General DPS set
            """
        )
        embed.add_field(
            name="Memories", 
            values="""
            4x Derketo
            2x Cottie
            """
        )
        embed.add_field(
            name="Memory Resonances", 
            values="""
            Top Slot: 6x HP/ATK +15 or ATK/DEF +15
            Bottom Slot: 6x Signature
            """
        )
        embed.add_field(
            name="Harmony Recommendation", 
            values="Cottie"
        )
        
        # for item in data:
        #     embed.add_field(name=item, value=item, inline=False)
        return embed

    # async def update_message(self,data):
    #     # self.update_buttons()
    #     await self.message.edit(embed=self.create_embed(data), view=self)

    # def update_buttons(self):
    #     if self.current_page == 1:
    #         self.first_page_button.disabled = True
    #         self.prev_button.disabled = True
    #         self.first_page_button.style = discord.ButtonStyle.gray
    #         self.prev_button.style = discord.ButtonStyle.gray
    #     else:
    #         self.first_page_button.disabled = False
    #         self.prev_button.disabled = False
    #         self.first_page_button.style = discord.ButtonStyle.green
    #         self.prev_button.style = discord.ButtonStyle.primary

    #     if self.current_page == int(len(self.data) / self.sep) + 1:
    #         self.next_button.disabled = True
    #         self.last_page_button.disabled = True
    #         self.last_page_button.style = discord.ButtonStyle.gray
    #         self.next_button.style = discord.ButtonStyle.gray
    #     else:
    #         self.next_button.disabled = False
    #         self.last_page_button.disabled = False
    #         self.last_page_button.style = discord.ButtonStyle.green
    #         self.next_button.style = discord.ButtonStyle.primary

    def get_current_page_data(self):
        until_item = self.current_page * self.sep
        from_item = until_item - self.sep
        if not self.current_page == 1:
            from_item = 0
            until_item = self.sep
        if self.current_page == int(len(self.data) / self.sep) + 1:
            from_item = self.current_page * self.sep - self.sep
            until_item = len(self.data)
        return self.data[from_item:until_item]
    
    @discord.ui.select(
        cls=discord.ui.Select,
        options=[discord.SelectOption(emoji=f"{chr(127462 + i)}", label=f"{chr(65 + i)}") for i in range(26)][:25],
        placeholder="Select a letter",
        min_values=1,
        max_values=1,
    )
    async def select(self, interaction: discord.Interaction, select: discord.ui.Select) -> None:
        await interaction.response.defer()
        await interaction.followup.send(f"You selected {select.values[0]}", ephemeral=True)
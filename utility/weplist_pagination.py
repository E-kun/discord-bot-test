from __future__ import annotations

import logging
import discord
import typing
import traceback
from utility.embedconfig import EmbedClass

class WeaponListPaginationView(discord.ui.View):
    message: discord.Message | None = None
    current_page = 0

    def __init__(self, user: discord.User | discord.Member, timeout: float = 60.0, data = []) -> None:
        super().__init__(timeout=timeout)
        self.user = user
        self.data = data
        self.weaponlistcount = len(self.data)
        self.embedconf = EmbedClass()
        self.update_buttons()

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
    
    # do stuff on timeout
    # async def on_timeout(self) -> None:
    #     # this method is called when the period mentioned in timeout kwarg passes.
    #     # we can do tasks like disabling buttons here.
    #     for button in self.children:
    #         button.disabled = True  # type: ignore
    #     # and update the message with the update View.
    #     if self.message:
    #         await self.message.edit(view=self)

    def create_embed(self):
        embed = {}
        
        embed = self.embedconf.create_list_embed(name=self.data[self.current_page]['name'], items=self.data[self.current_page]['list'], curpage=self.current_page + 1, maxlistcount=len(self.data))
        return embed

    @discord.ui.button(label="|<", style=discord.ButtonStyle.green)
    async def first_page_button(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        self.current_page=0
        embed = self.create_embed()
        self.update_buttons()
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="<", style=discord.ButtonStyle.blurple)
    async def prev_button(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        self.current_page-=1
        embed = self.create_embed()
        self.update_buttons()
        await interaction.response.edit_message(embed=embed, view=self)
        
    @discord.ui.button(label=">", style=discord.ButtonStyle.blurple)
    async def next_button(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        self.current_page+=1
        embed = self.create_embed()
        self.update_buttons()
        await interaction.response.edit_message(embed=embed, view=self)
        
    @discord.ui.button(label=">|", style=discord.ButtonStyle.green)
    async def last_page_button(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        self.current_page = int(len(self.data)) - 1
        embed = self.create_embed()
        self.update_buttons()
        await interaction.response.edit_message(embed=embed, view=self)
        

    def update_buttons(self):
        if self.current_page == 0:
            self.first_page_button.disabled = True
            self.prev_button.disabled = True
            self.first_page_button.style = discord.ButtonStyle.gray
            self.prev_button.style = discord.ButtonStyle.gray
        else:
            self.first_page_button.disabled = False
            self.prev_button.disabled = False
            self.first_page_button.style = discord.ButtonStyle.green
            self.prev_button.style = discord.ButtonStyle.primary

        if self.current_page == len(self.data) - 1:
            self.next_button.disabled = True
            self.last_page_button.disabled = True
            self.last_page_button.style = discord.ButtonStyle.gray
            self.next_button.style = discord.ButtonStyle.gray
        else:
            self.next_button.disabled = False
            self.last_page_button.disabled = False
            self.last_page_button.style = discord.ButtonStyle.green
            self.next_button.style = discord.ButtonStyle.primary

    # error handler for the view
    async def on_error(
        self, interaction: discord.Interaction[discord.Client], error: Exception, item: discord.ui.Item[typing.Any]
    ) -> None:
        tb = "".join(traceback.format_exception(type(error), error, error.__traceback__))
        message = f"An error occurred while processing the interaction for {str(item)}:\n```py\n{tb}\n```"
        await interaction.response.send_message(message)
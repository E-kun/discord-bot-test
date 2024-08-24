from __future__ import annotations

import logging
import discord
import typing
import traceback

class Button(discord.ui.Button):
    def __init__(self):
        super().__init__(style=discord.ButtonStyle.secondary, label="Test")

    # This function is called whenever this particular button is pressed
    # This is part of the "meat" of the game logic
    async def callback(self, interaction: discord.Interaction):
        assert self.view is not None
        view: PaginationView = self.view

        content = "Test"

        await interaction.response.edit_message(content=content, view=view)

class PaginationView(discord.ui.View):
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
            await self.update_message(self.data[:self.sep])
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

    def create_embed(self, data):
        embed = discord.Embed(title=f"User List Page {self.current_page} / {int(len(self.data) / self.sep) + 1}")
        for item in data:
            embed.add_field(name=item, value=item, inline=False)
        return embed

    async def update_message(self,data):
        self.update_buttons()
        await self.message.edit(embed=self.create_embed(data), view=self)

    def update_buttons(self):
        if self.current_page == 1:
            self.first_page_button.disabled = True
            self.prev_button.disabled = True
            self.first_page_button.style = discord.ButtonStyle.gray
            self.prev_button.style = discord.ButtonStyle.gray
        else:
            self.first_page_button.disabled = False
            self.prev_button.disabled = False
            self.first_page_button.style = discord.ButtonStyle.green
            self.prev_button.style = discord.ButtonStyle.primary

        if self.current_page == int(len(self.data) / self.sep) + 1:
            self.next_button.disabled = True
            self.last_page_button.disabled = True
            self.last_page_button.style = discord.ButtonStyle.gray
            self.next_button.style = discord.ButtonStyle.gray
        else:
            self.next_button.disabled = False
            self.last_page_button.disabled = False
            self.last_page_button.style = discord.ButtonStyle.green
            self.next_button.style = discord.ButtonStyle.primary

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

    # adding a component using it's decorator
    @discord.ui.button(label="|<", style=discord.ButtonStyle.green, )
    async def first_page_button(self, inter: discord.Interaction, button: discord.ui.Button[PaginationView]) -> None:
        self.current_page=1
        # button.label = str(self.count)
        # await inter.response.edit_message(view=self)
        await self.update_message(self.get_current_page_data())

    @discord.ui.button(label="<", style=discord.ButtonStyle.primary, )
    async def prev_button(self, inter: discord.Interaction, button: discord.ui.Button[PaginationView]) -> None:
        self.current_page-=1
        # button.label = str(self.count)
        await self.update_message(self.get_current_page_data())

    @discord.ui.button(label=">", style=discord.ButtonStyle.primary, )
    async def next_button(self, inter: discord.Interaction, button: discord.ui.Button[PaginationView]) -> None:
        self.current_page+=1
        # button.label = str(self.count)
        await self.update_message(self.get_current_page_data())

    @discord.ui.button(label=">|", style=discord.ButtonStyle.green, )
    async def last_page_button(self, inter: discord.Interaction, button: discord.ui.Button[PaginationView]) -> None:
        self.current_page = int(len(self.data) / self.sep) + 1
        # button.label = str(self.count)
        await self.update_message(self.get_current_page_data())

    # error handler for the view
    async def on_error(
        self, interaction: discord.Interaction[discord.Client], error: Exception, item: discord.ui.Item[typing.Any]
    ) -> None:
        tb = "".join(traceback.format_exception(type(error), error, error.__traceback__))
        message = f"An error occurred while processing the interaction for {str(item)}:\n```py\n{tb}\n```"
        await interaction.response.send_message(message)
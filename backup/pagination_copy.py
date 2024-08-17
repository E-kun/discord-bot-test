from __future__ import annotations

import logging
import discord
import typing
import traceback

class PaginationView(discord.ui.View):
    message: discord.Message | None = None
    count = 0

    def __init__(self, user: discord.User | discord.Member, timeout: float = 60.0) -> None:
        super().__init__(timeout=timeout)
        self.user = user

    # checks for the view's interactions
    async def interaction_check(self, interaction: discord.Interaction[discord.Client]) -> bool:
        # this method should return True if all checks pass, else False is returned
        # for example, you can check if the interaction was created by the user who
        # ran the command:
        if interaction.user == self.user:
            return True
        # else send a message and return False
        await interaction.response.send_message(f"The command was initiated by {self.user.mention}", ephemeral=True)
        return False

    # do stuff on timeout
    async def on_timeout(self) -> None:
        # this method is called when the period mentioned in timeout kwarg passes.
        # we can do tasks like disabling buttons here.
        for button in self.children:
            button.disabled = True  # type: ignore
        # and update the message with the update View.
        if self.message:
            await self.message.edit(view=self)

    # adding a component using it's decorator
    @discord.ui.button(label="0", style=discord.ButtonStyle.green, )
    async def counter(self, inter: discord.Interaction, button: discord.ui.Button[PaginationView]) -> None:
        self.count+=1
        button.label = str(self.count)
        await inter.response.edit_message(view=self)

    # error handler for the view
    async def on_error(
        self, interaction: discord.Interaction[discord.Client], error: Exception, item: discord.ui.Item[typing.Any]
    ) -> None:
        tb = "".join(traceback.format_exception(type(error), error, error.__traceback__))
        message = f"An error occurred while processing the interaction for {str(item)}:\n```py\n{tb}\n```"
        await interaction.response.send_message(message)
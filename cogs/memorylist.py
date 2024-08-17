
from __future__ import annotations

import typing
import traceback
import discord
import os
from discord.ext import commands
from discord.ext.commands import BucketType, cog, BadArgument, command, cooldown
from embedconfig import EmbedClass
# from pagination import BaseView

from discord.ui.select import BaseSelect

class Button(discord.ui.Button['MemoryList']):
    def __init__(self):
        super().__init__(style=discord.ButtonStyle.secondary, label="Test")

    # This function is called whenever this particular button is pressed
    # This is part of the "meat" of the game logic
    async def callback(self, interaction: discord.Interaction):
        assert self.view is not None
        view: BaseView = self.view

        content = "Test"

        await interaction.response.edit_message(content=content, view=view)

class BaseView(discord.ui.View):
    # interaction: discord.Interaction | None = None
    # message: discord.Message | None = None

    def __init__(self):
        super().__init__()
        self.add_item(Button())
        # super().__init__(timeout=timeout)
        # self.user = user

    # async def interaction_check(self, interaction: discord.Interaction) -> bool:
    #     if interaction.user.id != self.user.id:
    #         await interaction.response.send_message(
    #             "You cannot interact with this view.", ephemeral=True
    #         )
    #         return False
    #     self.interaction = interaction
    #     return True


    # def _disable_all(self) -> None:
    #     for item in self.children:
    #         if isinstance(item, discord.ui.Button) or isinstance(item, BaseSelect):
    #             item.disabled = True


    # async def _edit(self, **kwargs: typing.Any) -> None:
    #     if self.interaction is None and self.message is not None:
    #         await self.message.edit(**kwargs)
    #     elif self.interaction is not None:
    #         try:
    #             await self.interaction.response.edit_message(**kwargs)
    #         except discord.InteractionResponded:
    #             await self.interaction.edit_original_response(**kwargs)

    # async def on_error(self, interaction: discord.Interaction, error: Exception, item: discord.ui.Item[BaseView]) -> None:
    #     tb = "".join(traceback.format_exception(type(error), error, error.__traceback__))
    #     message = f"An error occurred while processing the interaction for {str(item)}:\n```py\n{tb}\n```"
    #     self._disable_all()
    #     await self._edit(content=message, view=self)
    #     self.stop()

    # async def on_timeout(self) -> None:
    #     self._disable_all()
    #     await self._edit(view=self)


class MemoryList(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print('MemoryList loaded.')

    @commands.command()
    async def memorylist(self, ctx: commands.Context) -> None:
        # print(dir(ctx))
        testview = BaseView()
        await ctx.send("Testing", view=testview)
        # print(dir(view))
        # testview.add_item(discord.ui.Button(label="Test", style=discord.ButtonStyle.blurple))
        # testview.message = await ctx.send("Testing", view=testview)
        # print(testview.message)
        


async def setup(bot: commands.Bot):
    await bot.add_cog(MemoryList(bot))
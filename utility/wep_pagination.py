from __future__ import annotations

import logging
import discord
import typing
import traceback
from utility.embedconfig import EmbedClass

class WeaponPageView(discord.ui.View):
    def __init__(self, user: discord.User | discord.Member, timeout: float = 60.0, weapon_box = []) -> None:
        super().__init__(timeout=timeout)
        self.user = user
        self.embedconfig = EmbedClass()
        self.weapon_box = weapon_box
        self.remove_item(self.two_star)
        self.remove_item(self.three_star)
        self.remove_item(self.four_star)
        self.remove_item(self.five_star)
        self.remove_item(self.six_star)

        for i in self.weapon_box:
            if(i['rarity'] == 2):
                self.add_item(self.two_star)
            elif(i['rarity'] == 3):
                self.add_item(self.three_star)
            elif(i['rarity'] == 4):
                self.add_item(self.four_star)
            elif(i['rarity'] == 5):
                self.add_item(self.five_star)
            else:
                self.add_item(self.six_star)

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

    def create_embed(self, rarity):
        embed = {}

        for weapon in self.weapon_box:
            if weapon['rarity'] == rarity:
                embed = self.embedconfig.create_weapon_embed(weapon)
        # for item in data:
        #     embed.add_field(name=item, value=item, inline=False)
        return embed


    @discord.ui.button(label="2★", style=discord.ButtonStyle.gray)
    async def two_star(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        self.two_star.style = discord.ButtonStyle.blurple
        self.current_page="2★"
        self.update_buttons()
        embed = self.create_embed(2)
        # print(dir(self))
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="3★", style=discord.ButtonStyle.gray)
    async def three_star(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        self.three_star.style = discord.ButtonStyle.blurple
        self.current_page="3★"
        self.update_buttons()
        embed = self.create_embed(3)
        # print(dir(self))
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="4★", style=discord.ButtonStyle.gray)
    async def four_star(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        self.four_star.style = discord.ButtonStyle.blurple
        self.current_page="4★"
        self.update_buttons()
        embed = self.create_embed(4)
        # self.update_buttons()
        # print(dir(self))
        await interaction.response.edit_message(embed=embed, view=self)
        
    @discord.ui.button(label="5★", style=discord.ButtonStyle.gray)
    async def five_star(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        self.five_star.style = discord.ButtonStyle.blurple
        self.current_page="5★"
        self.update_buttons()
        embed = self.create_embed(5)
        # self.update_buttons()
        # print(dir(self))
        await interaction.response.edit_message(embed=embed, view=self)
        
    @discord.ui.button(label="6★", style=discord.ButtonStyle.gray)
    async def six_star(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        self.six_star.style = discord.ButtonStyle.blurple
        self.current_page="6★"
        self.update_buttons()
        embed = self.create_embed(6)
        # self.update_buttons()
        # print(dir(self))
        await interaction.response.edit_message(embed=embed, view=self)

    def update_buttons(self):
        match self.current_page:
            case "2★":
                self.two_star.style = discord.ButtonStyle.blurple
                self.three_star.style = discord.ButtonStyle.gray
                self.four_star.style = discord.ButtonStyle.gray
                self.five_star.style = discord.ButtonStyle.gray
                self.six_star.style = discord.ButtonStyle.gray
            case "3★":
                self.two_star.style = discord.ButtonStyle.gray
                self.three_star.style = discord.ButtonStyle.blurple
                self.four_star.style = discord.ButtonStyle.gray
                self.five_star.style = discord.ButtonStyle.gray
                self.six_star.style = discord.ButtonStyle.gray
            case "4★":
                self.two_star.style = discord.ButtonStyle.gray
                self.three_star.style = discord.ButtonStyle.gray
                self.four_star.style = discord.ButtonStyle.blurple
                self.five_star.style = discord.ButtonStyle.gray
                self.six_star.style = discord.ButtonStyle.gray
            case "5★":
                self.two_star.style = discord.ButtonStyle.gray
                self.three_star.style = discord.ButtonStyle.gray
                self.four_star.style = discord.ButtonStyle.gray
                self.five_star.style = discord.ButtonStyle.blurple
                self.six_star.style = discord.ButtonStyle.gray
            case "6★":
                self.two_star.style = discord.ButtonStyle.gray
                self.three_star.style = discord.ButtonStyle.gray
                self.four_star.style = discord.ButtonStyle.gray
                self.five_star.style = discord.ButtonStyle.gray
                self.six_star.style = discord.ButtonStyle.blurple
            # case _:


    # def get_current_page_data(self):
    #     until_item = self.current_page * self.sep
    #     from_item = until_item - self.sep
    #     if not self.current_page == 1:
    #         from_item = 0
    #         until_item = self.sep
    #     if self.current_page == int(len(self.data) / self.sep) + 1:
    #         from_item = self.current_page * self.sep - self.sep
    #         until_item = len(self.data)
    #     return self.data[from_item:until_item]



    # error handler for the view
    async def on_error(
        self, interaction: discord.Interaction[discord.Client], error: Exception, item: discord.ui.Item[typing.Any]
    ) -> None:
        tb = "".join(traceback.format_exception(type(error), error, error.__traceback__))
        message = f"An error occurred while processing the interaction for {str(item)}:\n```py\n{tb}\n```"
        await interaction.response.send_message(message)
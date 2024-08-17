import discord

class EmbedClass:
    def __init__(self, message, title):
        self.embed = discord.Embed(
                title=title, 
                description=message,
                color=discord.Colour.blue(),
            )

    # def get_embed(self):
    #     return self.embed
    
    # def set_embed(self):
    #     embed = discord.Embed(
    #             title="Test Embed", 
    #             description="This is a test embed",
    #             color=discord.Colour.blue(),
    #         )
import discord

class EmbedClass:
    # def __init__(self, message, title):
    #     self.embed = discord.Embed(
    #             title=title, 
    #             description=message,
    #             color=discord.Colour.blue(),
    #         )

    def choose_build(self, build_array, choice):
        #Receive string based on choice and then compare to see which build has been selected. Return build object after check has been done
        # print(build_array, choice)
        for i in build_array:
            if choice == i['set_name']:
                build = i
                

        return build


    def create_build_embed(self, build, choice): 
        #Split build object here into 2 parts; first being the unchanging data fields (name + frame) and the second being the build choice

        name = build['unit_name']
        frame = build['frame_name']
        thumbnail_url = build['thumbnail_url']
        builds = build['builds']

        selection = self.choose_build(builds, choice)
        description = "\n".join(selection['description'])
        memories = "\n".join(selection['memories'])
        memory_resonance = "\n".join(selection['memory_resonance'])

        embed = discord.Embed(
            title=f"{name}: {frame}",
            description=f"{selection['set_type']}",
        )
        embed.add_field(name="Usage", value="Main")
        embed.add_field(name="Game Modes", value="Pain Cage, Warzone, Norman, Clash Reflection, High Difficulty")
        embed.add_field(
            name="Description", 
            value=description,
            inline=False
        )
        embed.add_field(
            name="Memories", 
            value=memories,
            inline=False
        )
        embed.add_field(
            name="Memory Resonances", 
            value=memory_resonance,
            inline=False
        )
        embed.add_field(
            name="Harmony Recommendation", 
            value=f"{selection['harmony_rec']}",
            inline=False
        )
        embed.set_thumbnail(url=thumbnail_url)
        return embed

    def create_memory_embed():
        ""

    def create_weapon_embed():
        ""

    def create_cub_embed():
        ""

    def create_skills_embed():
        ""

    def create_list_embed():
        ""

    def create_about_embed():
        ""
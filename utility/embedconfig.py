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

    def choose_cub_skills(self, active, passive, choice):
        if(choice == "active"):
            return active
        else:
            return passive

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
            description=f"{selection['set_type'] + " " + "Set"}"
        )
        embed.add_field(name="Usage", value=selection['set_type'])
        embed.add_field(name="Game Modes", value=selection['game_modes'])
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

    def create_memory_embed(self, memory):
        
        # print(memory['rarity'])
        stars = memory['rarity']
        
        match stars:
            case 2:
                stars = "★★"
                colour = 0x75d17d
            case 3:
                stars = "★★★"
                colour = 0x3c76bd
            case 4:
                stars = "★★★★"
                colour = 0xd667f0
            case 5:
                stars = "★★★★★"
                colour = 0xf79514
            case 6:
                stars = "★★★★★★"
                colour = 0xfc5f21

        embed = discord.Embed(
            title=f"{memory['name']} {stars}",
            # description=f"{memory['weapon_type']}",
            color=discord.Color(colour)
        )
        embed.add_field(
            name=f"2pc Set Bonus",
            value=f"{memory['2pc']}",
            inline=False
        )
        if (memory['4pc'] == ""):
            a = ""
        else:
            embed.add_field(
                name=f"4pc Set Bonus",
                value=f"{memory['4pc']}",
                inline=False
            )

        if ('6pc' in memory):
            embed.add_field(
                name=f"6pc Set Bonus",
                value=f"{memory['6pc']}",
                inline=False
            )
        else:
            a = ""
        
        embed.add_field(
            name="ATK",
            value=f"{memory['atk']}",
        )
        embed.add_field(
            name="CRIT",
            value=f"{memory['crit']}",
        ),
        embed.add_field(
            name="DEF",
            value=f"{memory['def']}",
        )
        embed.add_field(
            name="HP",
            value=f"{memory['hp']}",
        )
        embed.set_thumbnail(url=memory['thumbnail'])
        return embed

    def create_weapon_embed(self, weapon):
        effect = weapon['effect']
        stars = weapon['rarity']
        
        match stars:
            case 2:
                stars = "★★"
                colour = 0x75d17d
            case 3:
                stars = "★★★"
                colour = 0x3c76bd
            case 4:
                stars = "★★★★"
                colour = 0xd667f0
            case 5:
                stars = "★★★★★"
                colour = 0xf79514
            case 6:
                stars = "★★★★★★"
                colour = 0xfc5f21

        embed = discord.Embed(
            title=f"{weapon['name']} {stars}",
            description=f"{weapon['weapon_type']}",
            color=discord.Color(colour)
        )
        embed.add_field(
            name=f"{effect['effect_name']}",
            value=f"{effect['effect_desc']}",
            inline=False
        ),
        embed.add_field(
            name="ATK",
            value=f"{weapon['atk']}",
        ),
        embed.add_field(
            name="CRIT",
            value=f"{weapon['crit']}",
        ),
        embed.set_thumbnail(url=weapon['thumbnail'])
        return embed

    def create_cub_embed(self, cub, choice):
        
        active_skills = cub['active_skills']
        passive_skills = cub['passive_skills']

        if(choice == "active"):
            name = "**Active Skills**"
        else:
            name = "**Passive Skills**"

        skills = self.choose_cub_skills(active_skills, passive_skills, choice)

        embed = discord.Embed(
            title=f"{cub['name']}",
            description=f"{cub['cub_type']}",
            # color=discord.colour(value=0xfc5f21)
        )
        embed.set_thumbnail(url=cub['thumbnail'])
        embed.add_field(
                name=name,
                value="",
                inline=False
            )
        for i in skills:
            embed.add_field(
                name=i['skill_name'], 
                value=i['skill_desc'],
                inline=False
            )
        return embed

    def create_skills_embed(self, skill, skill_type):
        match skill_type:
            case "basic" | "red" | "blue" | "yellow" | "signature":
                print(skill)

                for i in skill:
                    embed = discord.Embed(
                        title=f"{i['name']}",
                        description=f""
                    )

                    embed.add_field(
                        name="Trigger",
                        value=f"{i['button_press']}",
                        inline=False
                    )

                    description = i['description']
                    embed.add_field(
                        name="",
                        value=f"{description['desc']}",
                        inline=False
                    )
                    embed.add_field(
                        name="",
                        value=f"{description['result']}",
                        inline=False)
            case "qte" | "leader" | "class":
                embed = discord.Embed(
                    title=f"{skill['name']}",
                    description=f""
                )
                description = skill['description']
                embed.add_field(
                    name="",
                    value=f"{description['desc']}",
                    inline=False
                )
                for i in description['result']:
                    embed.add_field(
                        name="",
                        value=f"{i}",
                        inline=False
                    )
            case "ss" | "sss" | "s+":
                embed = discord.Embed(
                    title=f"{skill['name']}",
                    description=f""
                )

                levels = skill['levels']

                for i in levels:
                    embed.add_field(
                        name=f"{i['rank']}",
                        value=f"{i['desc']}",
                        inline=False
                    )
        
        return embed

    def create_corepassive_embed(self, skill, ability_no):
        # print(skill)
        embed = discord.Embed(
            title=f"Core Passive - {skill['name']}",
            description=f""
        )

        ability = skill['skills'][ability_no]
            
        # print(ability)

        description = ability['description']
        result = description['result']
        desc_paragraph = description['desc']
        trigger = ""

        print(ability['name'])
        print(ability['button_press'])
        print(desc_paragraph)
        print(result)

        if ability['button_press'] == "N/A":
            trigger = ""
        else:
            trigger = f"Trigger: {ability['button_press']}"

        embed.add_field(
            name=f"Ability: {ability['name']}",
            value=trigger,
            inline=False
        )

        for i in desc_paragraph:               
            embed.add_field(
                name="",
                value=f"{i}",
                inline=False
            )

        if(len(result) > 0):
            for j in result:
                embed.add_field(
                    name="",
                    value=f"{j}",
                    inline=False
                )

        embed.set_footer(text=f"Part {ability_no + 1}/{len(skill['skills'])}")
        return embed

    def create_cublist_embed(self, cubs):
        embed = discord.Embed(
            title=f"List of CUBs",
            description="",
            color=discord.Color(0x3d6e41)
        )
        for cub in cubs:
            if(cub['sig_character'] != "N/A"):
                embed.add_field(
                    name="",
                    value=f"`{cub['base_rank']}・{cub['name']}  ({cub['sig_character']})`",
                    inline=False
                )
            else:
                embed.add_field(
                    name="",
                    value=f"`{cub['base_rank']}・{cub['name']}`",
                    inline=False
                )
        return embed

    def create_list_embed(self, name, items, curpage, maxlistcount):

        embed = discord.Embed(
            title=f"List of {name}",
            description="",
            color=discord.Color(0xb8f2e4)
        )
        for i in items:
            embed.add_field(
                name = "",
                value = i.replace('#', '★'),
                inline=False
            )
        embed.set_footer(text=f"Page {curpage}/{maxlistcount}")
        return embed

    def create_about_embed(self):
        embed = discord.Embed(
            title=f"About this Bot",
            description=f"Hi Commandant! I'm Celica, your guide to Babylonia and the world of Punishing: Gray Raven."
        )
        embed.add_field(
            name="Disclaimer",
            value=f"This bot is a community project initiated by Ek(#ek3970). It is not in any way affiliated with Kuro Games or their staff. If you would like to ask questions about the bot, please send me a DM or ping me on the Punishing: Gray Raven Official Discord. (Also Scire is not best girl. I was just held at gunpoint to give her that nickname.)",
            inline=False
        )
        embed.add_field(
            name="Credits",
            value=f"""
                Thanks to all of you who have helped out in the making of this bot. Without you it would have taken me much longer to get this off the ground.

                The dalaos for their build expertise:
                    Aethervoid
                    trs
                    pwowq
                    Hyperbrick
                    MstrPikachu
                    FabioJo40
                    KURAIMAKSU
            """,
            inline=False
        )
        embed.add_field(
            name = "",
            value = """ 
                Those who helped gather data for the bot:
                    Hyperbrick
                    FabioJo40
                    Miku (Yes that includes you Ms. Misinfo)

                The ones who came up with the nicknames for builds:
                    Aurora
                    Miku
                    MstrPikachu
                    trs

                The ones who helped with figuring out the EXPPC score equation:
                    Nova(blacknovatech)
                    CryoZero
                    Frustal
                    
                (This list is not limited btw. If your name is not on here and you have helped with this please send me a DM and I'll add you here. Otherwise if you helped but don't want to be mentioned thank you as well.)

                Huge thanks to Nova(Creator of the Huaxu site) for letting me reference his assets(images) for everything on this bot.

                Indirect thanks to Doomy for creating Cogs for me to create this bot.
            """,
            inline=False
        )
        return embed
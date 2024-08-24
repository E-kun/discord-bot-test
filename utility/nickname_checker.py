def check_nickname(nickname, caller): 
    match nickname:
        case "lumi" | "luminance":
            character = "luminance"
            weapon = ""
            cub = ""
        case "evil liv" | "seggs" | "green jumper" | "<:evilliv:1272415890453041223>" | "lux":
            character = "lux"
            weapon = ""
            cub = ""
        case "empy" | "solaeter" | "empyrea":
            character = "empyrea"
            weapon = ""
            cub = ""
        case "daren" | "bonka" | "tsundere" | "radiant daybreak" | "trs" | "<:trs:1275701510293946482>" | "bunny" | "bnnuy" | "scire":
            character = "scire"
            weapon = "illuminare"
            cub = ""
        case "capri" | "crapi" | "schizo" | "cappuccino" | "soup" | "pwowq":
            character = "capriccio"
            weapon = "sarastro"
            cub = ""
        case "uncle" | "king engine" | "kingengine" | "wata" | "epitaph":
            character = "epitaph"
            weapon = ""
            cub = ""
        case "supercar" | "car" | "hyper" | "hyperreal":
            character = "hyperreal"
            weapon = ""
            cub = ""
        case "cow" | "kale" | "kaleido":
            character = "kaleido"
            weapon = ""
            cub = ""
        case "lullaby" | "lost lullaby" | "feesh" | "fish" | "lamia":
            character = "lamia"
            weapon = "metis"
            cub = "cetus"
        case "weave" | "motivation" | "vergil's daughter" | "crimson weave":
            character = "crimson weave"
            weapon = ""
            cub = ""
        case "awoo" | "furry" | "feral" | "feral: 21" | "feral:21":
            character = "feral"
            weapon = ""
            cub = ""
        case "indomitus" | "noctis":
            character = "noctis"
            weapon = ""
            cub = ""
        case _:
            if(caller == "character"):
                character = nickname
            elif(caller == "weapon"):
                weapon = nickname
            else:
                cub = nickname

    if(caller == "character"):
        item_name = character
    elif(caller == "weapon"):
        item_name = weapon
    elif(caller == "cub"):
        item_name = cub

    return item_name

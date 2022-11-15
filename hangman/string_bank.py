logo = """
  _____   ____  _  ________ __  __  ____  _   _    _    _          _   _  _____ __  __          _   _
 |  __ \ / __ \| |/ /  ____|  \/  |/ __ \| \ | |  | |  | |   /\   | \ | |/ ____|  \/  |   /\   | \ | |
 | |__) | |  | | ' /| |__  | \  / | |  | |  \| |  | |__| |  /  \  |  \| | |  __| \  / |  /  \  |  \| |
 |  ___/| |  | |  < |  __| | |\/| | |  | | . ` |  |  __  | / /\ \ | . ` | | |_ | |\/| | / /\ \ | . ` |
 | |    | |__| | . \| |____| |  | | |__| | |\  |  | |  | |/ ____ \| |\  | |__| | |  | |/ ____ \| |\  |
 |_|     \____/|_|\_\______|_|  |_|\____/|_| \_|  |_|  |_/_/    \_\_| \_|\_____|_|  |_/_/    \_\_| \_| by nathzu
  \nSTART GAME (1)\n QUIT GAME (2)\n      HELP (3)
"""
# pokemon words for random choice
word_list = [
    "abra",
    "aerodactyl",
    "aggron",
    "alakazam",
    "arceus",
    "bagon",
    "bastiodon",
    "beldum",
    "blastoise",
    "bulbasaur",
    "butterfree",
    "cacnea",
    "camerupt",
    "cascoon",
    "caterpie",
    "celebi",
    "chansey",
    "charizard",
    "chikorita",
    "clawitzer",
    "cobalion",
    "conkeldurr",
    "cyndaquil",
    "darkrai",
    "delphox",
    "deoxys",
    "dialga",
    "dratini",
    "eevee",
    "ekans",
    "escavalier",
    "fennekin",
    "feraligatr",
    "floatzel",
    "flygon",
    "gallade",
    "garchomp",
    "gardevoir",
    "giratina",
    "greninja",
    "groudon",
    "grovyle",
    "hariyama",
    "haxorus",
    "heracross",
    "hydreigon",
    "jigglypuff",
    "larvitar",
    "lucario",
    "machamp",
    "magikarp",
    "meditite",
    "mudkip",
    "nidoking",
    "nidoqueen",
    "oshawott",
    "palkia",
    "patrat",
    "pikachu",
    "piplup",
    "pyukumuku",
    "quilava",
    "rayquaza",
    "reshiram",
    "rhyperior",
    "salamence",
    "samurott",
    "sceptile",
    "scyther",
    "snorlax",
    "spiritomb",
    "suicune",
    "swampert",
    "tentacruel",
    "terrakion",
    "thundurus",
    "togepi",
    "treecko",
    "tyranitar",
    "umbreon",
    "venomoth",
    "wobbufet",
    "wynaut",
    "xatu",
    "yveltal",
    "zeraora",
    "zubat",
    "zweilous",
]
#
stages = [
    """
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========
""",
    """
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========
""",
    """
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========
""",
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========""",
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========
""",
    """
    +---+
    |   |
    O   |
        |
        |
        |
  =========
""",
    """
    +---+
    |   |
        |
        |
        |
        |
  =========
""",
]

win = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣴⡶⠿⠛⠛⠛⠛⠛⠛⠻⠷⣦⣄⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⡾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠙⠿⣦⡀⠀⠀⠀
⠀⠀⢠⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠈⢿⣆⠀⠀
⠀⢠⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⢻⣇⠀
⠀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⣿⡄
⢠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⢸⡇
⠸⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀ ⣼⡇
⠀⣿⣿⣦⣀⠀⠀⠀⠀⠀⣠⣴⣶⢶⣦⣤⡀⠀⠀⠀⠀⢀⣠⣾⣿⠇
⠀⠸⣷⡈⠛⠿⣶⣦⣤⣼⠟⡡⠒⠒⢢⠙⣿⣤⣤⣶⠾⠟⠋⣰⡟⠀
⠀⠀⠹⣷⡄⠀⠀⠀⠉⣿⣄⠣⣀⢀⡠⢀⣿⠏⠁⠀⠀⢀⣴⡟⠀⠀
⠀⠀⠀⠈⠻⣦⣄⠀⠀⠈⠻⢷⣦⣤⣶⠿⠋⠀⠀⢀⣤⡾⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠛⠷⣦⣤⣀⣀⠀⠀⣀⣀⣠⣤⡶⠟⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠛⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀
"""

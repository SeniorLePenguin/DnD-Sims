import Visuals as vis
import pathlib as pth
import json

# We need to make a class containing characters

class character:
    def __init__(self, name = "NO NAME", background = ["Class", "Subclass", "Species", "Background", "LV"], stats = [0,0,0,0,0,0],
                 prepared = set(), fullSlots = [], currentSlots = [], equipment = {}):
        # Stores the name of the character
        self.name = name

        # Stores relevant details for the gameplay of the character
        self.background = background

        # Stores the stats of the character, we keep only the values of the 6 stats in order:
        # STR, DEX, CON, WIS, INT, CHAR
        self.stats = stats

        # Stores the list of prepared spells, we use a set for ease of use
        self.prepared = prepared

        # Stores the spell slots available to the character affter rest
        self.fullSlots = fullSlots

        # Stores the spell slots currently available to the character
        self.currentSlots = currentSlots

        # Stores equipment in a dictionary of item name and a string including a description
        # Since descriptions can be long, maybe store them in separate files?
        # Details to be figured out later
        self.equipment = equipment

        # Need to add a way to follow features and fears as well
        # But this is best left for the future

    # A function to open a window showing the summary information for the character
    def summary(self):
        vis.characterSummary(name = self.name, cl = self.background[0], subcl = self.background[1], species = self.background[2],
                             background = self.background[3], LV = self.background[4], stats = self.stats, prepared = self.prepared)


# This dictionary will store all the loaded characters along with their nicknames
loadedChars = {}


savePath = pth.Path("saves_DONT_TOUCH")
def loadChar(path):
    with open(path) as file:
        save = json.load(file)

        # Load every section of character details into a different object
        nickname = save["nickname"]
        charGeneral = save["general details"]
        charSpells = save["spell details"]

        charSpells["prepared spells"] = set(charSpells["prepared spells"])

        # Be CAREFUL to keep the arguent order the same for loadChar and
        # the character init functions!!
        loadedChars[nickname] = character(*charGeneral.values(), *charSpells.values())
        

# TESTS - do not include in commit, only for local checks

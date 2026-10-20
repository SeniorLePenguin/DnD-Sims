import Visuals as vis
import pathlib as pth
import json

# We need to make a class containing characters

class character:
    def __init__(self):
        # Stores the name of the character
        self.name = "NO NAME"

        # Stores relevant details for the gameplay of the character
        self.background = ["Class", "Subclass", "Species", "Background", "LV"]

        # Stores the stats of the character, we keep only the values of the 6 stats in order:
        # STR, DEX, CON, WIS, INT, CHAR
        self.stats = [0,0,0,0,0,0]

        # Stores the list of prepared spells, we use a set for ease of use
        self.prepared = set()

        # Stores the spell slots available to the character affter rest
        self.fullSlots = []

        # Stores the spell slots currently available to the character
        self.currentSlots = []

        # Stores equipment in a dictionary of item name and a string including a description
        # Since descriptions can be long, maybe store them in separate files?
        # Details to be figured out later
        self.equipment = {}

        # Need to add a way to follow features and fears as well
        # But this is best left for the future

    def summary(self):
        vis.characterSummary(self.name, *self.background)



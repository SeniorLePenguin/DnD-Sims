import Visuals

# We need to make a class containing characters

class character:
    def __init__(self):
        self.name = "NO NAME"
        self.background = ["Class", "Subclass", "Species", "Background"]
        self.stats = (0,0,0,0,0,0)
        self.prepared = set()
        self.slots = []
        self.equipment = {}

        # Need to add a way to follow features and fears as well
        # But this is best left for the future



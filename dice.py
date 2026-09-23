import random 


# region Core functions

# Returns a list of values of 'number' rolled dice with the given sides
def rollDice(sides = 20, number = 1):
    result = [random.randrange(1, sides + 1) for x in range(number)]
    return result


# Returns the sum of all values, as well as the rolls (Maybe add a fixed value bonus as well, though I prefer to keep it basic for now)
def diceSummer(number, sides):
    rolls = rollDice(number, sides)
    total = sum( rollDice(number, sides) )
    return (total, rolls)


# Returns the value of a general d20 check
def d20Check(mod = 0, prof = 0, adv = None):

    #Checks if we have adv/disadv (corresponds to True/False), and makes the relevant rolls.
    if adv is None:
        roll = rollDice()[0]
    else:
        rolls = rollDice(20,2)

        if adv:
            roll = max(rolls)
        else:
            roll = min(rolls)

    result = roll + mod + prof  #Adds the relevant ability modifier and proficiency (if applicable)
    return result    

#Function describing to the user what the spell effect is
def spellEffect(bool):
    if bool is None:
        return "only has an effect"
    elif bool:
        return "deals damage"
    else:
        return "heals HP"


# Make a class for spells. It contains properties for all the details of a spell.
class spell:
    def __init__(self, name, formula, hurt, LV, diceSides, diceNum, fixedMod, *, dmgType = None):

        self.name = name
        self.formula = formula
        self.hurt = bool(hurt)
        self.LV = int(LV)
        self.diceSides = int(diceSides)
        self.diceNum = int(diceNum)
        self.fixedMod = int(fixedMod)
        self.dmgType = dmgType

    #diceNum usually depends on character level, we record the minimum but need
    # a way to update it before it's called.
    def diceNumSynch(self, charLV):
        match self.formula:
            case "6Scaling":
                self.diceNum = 1 + (charLV + 1)//6

            case _:
                raise Exception("formula for the number of dice not recognised. \n Fix the \"formula\" section of the spell entry, or add new case in the diceNumSynch function")

#endregion



# region Data import

def HealOrHurt(word):
    match word:
        case "Heal":
            return False
        case "Dmg":
            return True

        case _:
            raise Exception("Unexpected value for the healing/damaging variable in the cvs")


spelldict = {}
with open("./SpellList.csv", "r") as spellData:
    next(spellData)

    for line in spellData:
        entries = line.strip('\n').split(",")

        spelldict[entries[0]] = spell(
            name = entries[0], 
            formula = entries [2], 
            hurt=HealOrHurt(entries[3]),
            LV = int(entries[4]),
            diceNum = int(entries[5]),
            diceSides = int(entries[6]),
            fixedMod = int(entries[7]),
            dmgType = entries[1]
            )

# endregion

# TESTS:
#REMEMBER - do NOT add tests to the staging area.

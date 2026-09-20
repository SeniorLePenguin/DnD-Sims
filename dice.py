import random 


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


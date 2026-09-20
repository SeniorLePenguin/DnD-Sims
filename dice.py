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

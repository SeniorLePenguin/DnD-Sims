import random 


# Returns a list of values of 'number' rolled dice with the given sides
def rollDice(number, sides):
    result = [random.randrange(1, sides + 1) for x in range(number)]
    return result


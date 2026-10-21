import tkinter as inter
import math


def characterSummary(name = '', cl = '', subcl = '', species = '', background = '', LV = 1, stats = [0,0,0,0,0,0]):
    window2 = inter.Tk()

    # Define an image - portrait of the character and display it top-left on the grid
    photo = inter.PhotoImage(file = "./CharPortrait.png")

    width = 200
    height = 200

    factor = max(1, math.ceil(photo.width() / width), math.ceil(photo.height() / height))
    photo = photo.subsample(factor)
    charPortrait = inter.Label(window2, 
                               image = photo, 
                               width = width,
                               height = height)
    
    charPortrait.grid(row = 0, column = 0, rowspan = 2)


    # Adds a label with the character's name
    # This label will be STATIC for the duration of the window instance
    nameLabel = inter.Label(window2, text = name)
    nameLabel.grid(row = 0, column = 1)

    # Adds a label with character details like clas and species
    # This label will be STATIC for the duration of the window instance
    mechanicsInfo = f"{cl} ({subcl}) {species} \n Background --> {background}"
    mechanicsLabel = inter.Label(window2, text = mechanicsInfo)
    mechanicsLabel.grid(row = 1, column = 1)



    # Adds a frame for the character statblock
    statDisplay = inter.Frame(window2)
    statDisplay.grid(row = 2, column = 0, rowspan = 2)

    # Then we display the actual stat values in the frame
    valuesText = (
        f"Strength: {stats[0]}\n"
        f"Dexterity: {stats[1]}\n"
        f"Constitution: {stats[2]}\n"
        f"Intelligence: {stats[3]}\n"
        f"Wisdom: {stats[4]}\n"
        f"Charisma: {stats[5]}"
    )
    statValues = inter.Label(statDisplay, text = valuesText)
    statValues.pack()


    #
    spells = inter.Text(window2, width = 40, height = 10)
    spells.grid(row = 3, column = 1)
    spells['state'] = 'disabled'

    window2.mainloop()



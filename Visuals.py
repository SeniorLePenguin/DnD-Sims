import tkinter as inter


def character_summary(name = '', cl = '', subcl = '', species = ''):
    window2 = inter.Tk()

    # Define an image - portrait of the character and display it top-left on the grid
    portraitSource = inter.PhotoImage(file = "./CharPortrait.png")
    charPortrait = inter.Label(window2, image = portraitSource)
    charPortrait.grid(row = 0, column = 0, rowspan = 2)

    # Adds a label with the character's name
    # This label will be STATIC for the duration of the window instance
    nameLabel = inter.Label(window2, text = name)
    nameLabel.grid(row = 0, column = 1)

    # Adds a label with character details like clas and species
    # This label will be STATIC for the duration of the window instance
    mechanicsInfo = f"{cl} ({subcl}) {species}"
    mechanicsLabel = inter.Label(window2, text = mechanicsInfo)
    mechanicsLabel.grid(row = 1, column = 1)

    # Adds a frame for the character statblock
    stats = inter.Frame(window2)
    stats.grid(row = 2, column = 0, rowspan = 2)

    #
    spells = inter.Text(window2, width = 40, height = 10)
    spells.grid(row = 4, column = 1)
    spells['state'] = 'disabled'

    window2.mainloop()



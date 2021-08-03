from tkinter import *
import pygame
pygame.init()

RES = (400, 400)

win = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

black = (0, 0, 0)
green = (50, 150, 50)
blue = (50, 50, 150)

currentColour = black
dummyVar = "black"

def drawFrame():
    win.fill(currentColour)

    pygame.display.update()

def chooseColor():

    def printAndSet(*args):
        print([x for x in args])
        print(color.get())
        setColour(color.get())

    tkWindow = Tk()
    tkWindow.geometry('400x400')

    color = StringVar(tkWindow, dummyVar)
    color.trace('w', printAndSet)

    dropDown = OptionMenu(tkWindow, color, "green", "blue", "black")
    dropDown.pack()

    button = Button(tkWindow, text="Done", command=tkWindow.destroy)
    button.pack()

    mainloop()

def testMe(*args):
    for x in args:
        print(x)

    print("Alllll DOney")

def setColour(chosenColor):
    global currentColour
    print(chosenColor, type(chosenColor))

    if chosenColor == "black":
        currentColour = black
    elif chosenColor == "blue":
        currentColour = blue
    elif chosenColor == "green":
        currentColour = green

running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            chooseColor()
        elif event.type == pygame.KEYDOWN:
            if event.unicode == 'p':
                print()

    drawFrame()
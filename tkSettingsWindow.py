from tkinter import *
from tkinter import messagebox, ttk

from backendStructure import *

def openSettings():

    def addScale(*args):
        global scalesDict, scaleNames, scale

        name = newScaleName.get()
        scaleString = newScaleNotes.get()

        if not name=="" and not scaleString=="":
            try:
                scaleArray = [int(n) for n in scaleString.split(',')]
                oldScales = readInScales()
                oldScales[name] = scaleArray

                with open('jsonScaleStorage.json', 'w') as file:
                    json.dump(oldScales, file)

                scalesDict = readInScales()
                scaleNames = [s for s in scalesDict]
                scale = StringVar(tkWindow, scaleNames[0])

                scaleOptions.update()


                
            except:
                print("That wasnt in the correct format deary")


    def showHelp(*args):
        messagebox.showinfo("Help", "To add a new scale, enter the name of the scale and the notes which make up the scale, with note #1 being the root note")

    def showError(*args):
        print("Not valid Scale")

    def checkValid(*args):
        if not newScaleNotes.get() == "":
            try:
                splitStringArray = [int(n) for n in newScaleNotes.get().split(',')]
                if max(splitStringArray) >= 12 or min(splitStringArray) <= 0:
                    # This is wrong -> ERROR
                    showError()
                else:
                    # Correct -> Remove Error
                    print("Thats good yeah")
            except:
                showError()

    tkWindow = Tk()
    tkWindow.geometry('290x230+500+500')
    tkWindow.title("Scaley")

    scalesDict = readInScales()
    scaleNames = [s for s in scalesDict]
    scale = StringVar(tkWindow, scaleNames[0])


    note = StringVar(tkWindow, allNotes[0])

    newScaleName = StringVar(tkWindow, "")
    newScaleNotes = StringVar(tkWindow, "")
    newScaleNotes.trace('w', checkValid)

    Label(tkWindow, text="Choose Scale:").grid(row=0, column=0, padx=10)
    Label(tkWindow, text="Root Note:").grid(row=1, column=0, padx=10)

    Label(tkWindow, text="Add New Scale:").grid(row=3, columnspan=2, padx=10)
    Label(tkWindow, text="Scale Name:").grid(row=4, column=0)
    Label(tkWindow, text="Notes (eg: 1,3,4,5,6):").grid(row=4, column=1)


    scaleOptions = OptionMenu(tkWindow, scale, *scaleNames)
    scaleOptions.grid(row=0, column=1, padx=10)

    noteOptions = OptionMenu(tkWindow, note, *allNotes)
    noteOptions.grid(row=1, column=1, padx=10)

    showLetter = IntVar() # IntVar is 0 or 1
    showLetterToggle = Checkbutton(tkWindow, text="Show Note Letters: ", variable=showLetter).grid(row=2, columnspan=2)

    scaleNameEntry = Entry(tkWindow, textvariable=newScaleName)
    scaleNameEntry.grid(row=5, column=0, padx=10)

    scaleNotesEntry = Entry(tkWindow, textvariable=newScaleNotes)
    scaleNotesEntry.grid(row=5, column=1, padx=10)

    Button(tkWindow, text="Add Scale", command=addScale).grid(row=7,column=0, pady=10)
    Button(tkWindow, text="Help", command=showHelp).grid(row=7,column=1)
    Button(tkWindow, text="Done", command=tkWindow.destroy).grid(row=8,columnspan=2)


    mainloop()
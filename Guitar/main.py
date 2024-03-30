notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
all_notes = []

for oct in range(7):
    for note in notes:
        all_notes.append(note + f"{oct}")
    
class String:
    def __init__(self, string_num, zero_note) -> None:
        self.string_num = string_num
        self.zero_note = zero_note

        self.fret_notes = self.getFretNotes()
    

    def getFretNotes(self):
        note_index = all_notes.index(self.zero_note)

        new_fret_notes = all_notes[note_index:note_index+12]

        return new_fret_notes

    def printFretNotes(self):
        string_text = f"{self.zero_note:>4} |"

        for i in range(1,len(self.fret_notes)):
            string_text += f"{self.fret_notes[i]:^7}+"

        print(string_text)

class FullNeck:
    def __init__(self, tuning):
        self.tuning = tuning
        self.strings = []

        for i in range(len(tuning)):
            new_string = String(i, tuning[i])
            self.strings.append(new_string)

    def printNeck(self):
        for s in self.strings[::-1]:
            s.printFretNotes()

        print("-"*95)
        
        num_string = "   0 |"

        for i in range(1,12):
            num_string += f"{i:^7}|"

        print(num_string)


tuning = ['E2','A2','D3','G3','B3','E4']

fretBoard = FullNeck(tuning)

fretBoard.printNeck()

import AppManager as AM

all_notes = AM.ALL_NOTES

open_note = 'e'

open_note_index = all_notes.index(open_note)

string_array = all_notes[open_note_index:] + all_notes[:open_note_index]

print(string_array)
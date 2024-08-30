import AppManager as AM

all_notes = AM.ALL_NOTES

open_note = 'b'

open_note_index = all_notes.index(open_note)

new_note = all_notes[(open_note_index+1) % len(all_notes)] 

print(new_note)
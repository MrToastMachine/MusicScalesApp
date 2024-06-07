from Object01 import Object01
import sources as srcs

sharps = [2,4,7,9,11,14,16,19,21,23] # from C to C
ALL_NOTES = ['c','c#','d','d#','e','f','f#','g','g#','a','a#','b']

srcs.readInScales()

maj_scale = srcs.scales["Major"]
root = 'g'

def getNotesInScale(root, scale):
    notes_in_scale = []
    root_pos = ALL_NOTES.index(root)
    for note_pos in scale:
        note_index = (root_pos + note_pos - 1) % len(ALL_NOTES)
        notes_in_scale.append(ALL_NOTES[note_index])
    
    return(notes_in_scale)

print(f"Root: {root}")
print("Scale:", maj_scale)

notes = getNotesInScale(root, maj_scale)

print(notes)

for note in ALL_NOTES:
    if notes.__contains__(note):
        print("GOO", note)


import pygame
import time
from colours import Colours
from AppManager import ALL_NOTES
from AppManager import FONT
import AppManager
from button import Button

from pygame import gfxdraw

DOT_POSITIONS = [3,5,7,9]
DOUBLE_DOT_POSITIONS = [12]

NOTE_FONT = AppManager.getFont(30)


def drawCircle(surface, color, border_color, pos, radius):
    x, y = pos
    gfxdraw.filled_circle(surface, round(x), round(y), round(radius), color)
    gfxdraw.aacircle(surface, round(x), round(y), round(radius), border_color)

def getStringArray(open_note):
    open_note_index = ALL_NOTES.index(open_note)
    return ALL_NOTES[open_note_index:] + ALL_NOTES[:open_note_index+1]
    
def getNoteNumber(note):
    if AppManager.ACTIVE_ROOT == None or AppManager.ACTIVE_SCALE == None:
        print("No scale and root note selected")
        return False
    
    notes_in_scale = AppManager.getNotesInScale(AppManager.ACTIVE_ROOT, AppManager.ACTIVE_SCALE)

    num_in_scale = notes_in_scale.index(note)+1

    return num_in_scale


class GuitarString():
    def __init__(self, str_num, open_note):
        self.str_num = str_num
        self.open_note = open_note

    def drawStringNotes(self, fretboard):

        self.string_array = getStringArray(self.open_note)
        
        centre_y = fretboard.y_padding + fretboard.string_gap * (0.5 + self.str_num - 1)
        open_note_xPos = fretboard.x_padding - fretboard.fret_spacing/2

        pygame.draw.line(fretboard.win, Colours.WHITE, (fretboard.x_padding, centre_y), (fretboard.x_padding + fretboard.neck_len, centre_y), 1)


        for i, note in enumerate(self.string_array):
            note_pos = open_note_xPos + i*fretboard.fret_spacing
            if i == 0:
                note_pos += fretboard.fret_spacing/4
            # pygame.draw.circle(fretboard.win, Colours.WHITE,(note_pos, centre_y), AppManager.NOTE_CIRCLE_RADIUS)

            special_note_colour = self.checkNoteHighlighted(note)
            note_colour = special_note_colour if special_note_colour else Colours.WHITE
            drawCircle(fretboard.win, note_colour, Colours.BLACK,(note_pos, centre_y), AppManager.NOTE_CIRCLE_RADIUS)

            if AppManager.SHOW_SCALE_NUMBERS and self.checkNoteHighlighted(note):
                note_num = str(getNoteNumber(note))
                note_label = NOTE_FONT.render(note_num, True, Colours.BLACK)
                note_label_size = NOTE_FONT.size(note_num)
                note_label_pos = (note_pos - note_label_size[0]/2 + 1, centre_y - note_label_size[1]/2 + 1)
            else:
                note_label = NOTE_FONT.render(note, True, Colours.BLACK)
                note_label_size = NOTE_FONT.size(note)
                note_label_pos = (note_pos - note_label_size[0]/2 + 1, centre_y - note_label_size[1]/2 + 1)

            fretboard.win.blit(note_label, note_label_pos)

    def checkNoteHighlighted(self, note):
        if AppManager.ACTIVE_ROOT == None or AppManager.ACTIVE_SCALE == None:
            return False
        
        notes_in_scale = AppManager.getNotesInScale(AppManager.ACTIVE_ROOT, AppManager.ACTIVE_SCALE)
        
        if notes_in_scale.__contains__(note):
            note_index = notes_in_scale.index(note)
            note_colour = Colours.SCALE_NOTES_COLORS[note_index]
            return note_colour
        else:
            return False





class Fretboard():
    def __init__(self, win, zone_width, zone_height, neck_len, neck_width, bg_color, neck_colour):
        self.win = win
        self.zone_height = zone_height
        self.zone_width = zone_width
        self.neck_len = neck_len
        self.neck_width = neck_width
        self.bg_color = bg_color
        self.neck_colour = neck_colour        

        self.x_padding = (zone_width - neck_len)/2
        self.y_padding = (zone_height - neck_width)/2

        self.string_gap = self.neck_width / 6

        self.all_strings = []

        self.createFretboard()

        # self.x_offset = x_padding
        # self.y_offset = y_padding

    def createFretboard(self):
        self.neck_rect = pygame.Rect(self.x_padding, self.y_padding, self.neck_len, self.neck_width)

        self.fret_spacing = self.neck_len/12

        for i, open_note in enumerate(AppManager.GUITAR_TUNING):
            self.all_strings.append(GuitarString(6 - i, open_note))


    def drawFretboard(self):
        print(f"Note circle radius: {AppManager.NOTE_CIRCLE_RADIUS}")

        # Draw Background colour
        pygame.draw.rect(self.win, self.bg_color, (0,0,self.zone_width, self.zone_height))

        if AppManager.ACTIVE_ROOT and AppManager.ACTIVE_SCALE:
            # Title showing current root note and scale
            active_setup_text = f"{AppManager.ACTIVE_ROOT} {AppManager.ACTIVE_SCALE}"
        else:
            active_setup_text = "No Scale Selected"
        text = FONT.render(active_setup_text, True, Colours.WHITE)

        font_size = FONT.size(active_setup_text)
        title_pos = ((self.zone_width - font_size[0])/2, (self.y_padding - font_size[1])/2)
        self.win.blit(text, title_pos)

        # Neck
        pygame.draw.rect(self.win, self.neck_colour, self.neck_rect)

        # Frets

        for i in range(13):
            fret_xPos = round(self.x_padding + i*self.fret_spacing)
            pygame.draw.line(self.win, Colours.GRAY, (fret_xPos, self.y_padding), (fret_xPos, self.y_padding + self.neck_width), 3)

            dist_above_neck = 10
            if DOT_POSITIONS.__contains__(i+1):
                dot_pos = (fret_xPos + self.fret_spacing/2, self.y_padding - dist_above_neck)
                pygame.draw.circle(self.win, Colours.BLACK, dot_pos, 3)

            elif DOUBLE_DOT_POSITIONS.__contains__(i+1):
                dot_1_pos = dot_pos = (fret_xPos + self.fret_spacing/3, self.y_padding - dist_above_neck)
                dot_2_pos = dot_pos = (fret_xPos + self.fret_spacing*2/3, self.y_padding - dist_above_neck)
                pygame.draw.circle(self.win, Colours.BLACK, dot_1_pos, 3)
                pygame.draw.circle(self.win, Colours.BLACK, dot_2_pos, 3)

        # Strings
        for string in self.all_strings:
            string.drawStringNotes(self)


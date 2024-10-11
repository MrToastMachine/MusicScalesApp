import pygame
import time
from colours import Colours
from AppManager import ALL_NOTES
from AppManager import FONT
import AppManager as AM
from button import Button

from pygame import gfxdraw

DOT_POSITIONS = [3,5,7,9]
DOUBLE_DOT_POSITIONS = [12]

NOTE_FONT = AM.getFont(30)

NUM_STRINGS = len(AM.GUITAR_TUNING)

TUNING_BOX_COLOR = Colours.WHITE
TUNING_LETTER_COLOR = Colours.BLACK


def drawCircle(surface, color, border_color, pos, radius):
    x, y = pos
    gfxdraw.filled_circle(surface, round(x), round(y), round(radius), color)
    gfxdraw.aacircle(surface, round(x), round(y), round(radius), border_color)

def getStringArray(open_note):
    open_note_index = ALL_NOTES.index(open_note)
    return ALL_NOTES[open_note_index:] + ALL_NOTES[:open_note_index+1]
    
def getNoteNumber(note):
    if AM.ACTIVE_ROOT == None or AM.ACTIVE_SCALE == None:
        print("No scale and root note selected")
        return False
    
    notes_in_scale = AM.getNotesInScale(AM.ACTIVE_ROOT, AM.ACTIVE_SCALE)

    num_in_scale = notes_in_scale.index(note)+1

    return num_in_scale

class LetterBox():
    def __init__(self, id, pos, size, letter, box_color, text_color):
        self.id = id
        self.rect = pygame.Rect(pos[0], pos[1], size, size)

        self.letter = letter

        self.box_color = box_color
        self.text_color = text_color
        self.font = AM.getFont(size - 10)

        self.up_arrow_rect = pygame.Rect(self.rect.left, self.rect.top - 20, self.rect.width, 15)
        self.down_arrow_rect = pygame.Rect(self.rect.left, self.rect.bottom + 5, self.rect.width, 15)

        self.up_verts = [self.up_arrow_rect.bottomleft, self.up_arrow_rect.bottomright, [self.up_arrow_rect.centerx, self.up_arrow_rect.top]]
        self.down_verts = [self.down_arrow_rect.topleft, self.down_arrow_rect.topright, [self.down_arrow_rect.centerx, self.down_arrow_rect.bottom]]
    
    def Draw(self, win):
        self.letter = AM.GUITAR_TUNING[self.id].capitalize()
        note_label = self.font.render(self.letter, True, self.text_color)
        note_label_size = self.font.size(self.letter)
        note_label_pos = (self.rect.centerx - note_label_size[0]/2 , self.rect.centery - note_label_size[1]/2 )

        pygame.draw.rect(win, self.box_color, self.rect)
        win.blit(note_label, note_label_pos)
        pygame.draw.polygon(win, Colours.BLACK, self.up_verts)
        pygame.draw.polygon(win, Colours.BLACK, self.down_verts)

    def CheckArrowClicks(self, mousePos):
        if self.up_arrow_rect.collidepoint(mousePos[0], mousePos[1]):
            print(self.id,"UP")
            current_note_index = ALL_NOTES.index(AM.GUITAR_TUNING[self.id])
            new_note = AM.ALL_NOTES[(current_note_index+1) % len(AM.ALL_NOTES)]
            AM.GUITAR_TUNING[self.id] = new_note

        elif self.down_arrow_rect.collidepoint(mousePos[0], mousePos[1]):
            print(self.id,"DOWN")
            current_note_index = AM.ALL_NOTES.index(AM.GUITAR_TUNING[self.id])
            new_note = AM.ALL_NOTES[(current_note_index-1) % len(AM.ALL_NOTES)]
            AM.GUITAR_TUNING[self.id] = new_note
        

class TuningSection():
    def __init__(self, pos, size, min_gap):
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])

        max_box_width = self.rect.width + min_gap * (NUM_STRINGS - 1) 
        self.box_size = min(self.rect.height, max_box_width)

        self.all_text_boxes = []
        self.CreateSection()

    def CreateSection(self):
        self.gap = (self.rect.width - NUM_STRINGS * self.box_size) / (NUM_STRINGS - 1)

        for i, str_tuning in enumerate(AM.GUITAR_TUNING):
            xPos = self.rect.left + i * (self.box_size + self.gap)
            yPos = self.rect.centery - (self.box_size / 2)
            lb = LetterBox(i, (xPos, yPos), self.box_size, str_tuning.capitalize(), TUNING_BOX_COLOR, TUNING_LETTER_COLOR)
            self.all_text_boxes.append(lb)

    def DrawSection(self, win):
        for lb in self.all_text_boxes:
            lb.Draw(win)



class GuitarString():
    def __init__(self, str_num, open_note):
        self.str_num = str_num
        self.open_note = open_note

    def drawStringNotes(self, fretboard):

        self.open_note = AM.GUITAR_TUNING[6-self.str_num]
        # print(self.str_num, self.open_note)
        self.string_array = getStringArray(self.open_note)
        
        centre_y = fretboard.y_padding + fretboard.string_gap * (0.5 + self.str_num - 1)
        open_note_xPos = fretboard.x_padding - fretboard.fret_spacing/2

        pygame.draw.line(fretboard.win, Colours.WHITE, (fretboard.x_padding, centre_y), (fretboard.x_padding + fretboard.neck_len, centre_y), 1)


        for i, note in enumerate(self.string_array):
            note_pos = open_note_xPos + i*fretboard.fret_spacing
            if i == 0:
                note_pos += fretboard.fret_spacing/4
            # pygame.draw.circle(fretboard.win, Colours.WHITE,(note_pos, centre_y), AM.NOTE_CIRCLE_RADIUS)

            special_note_colour = self.checkNoteHighlighted(note)
            note_colour = special_note_colour if special_note_colour else Colours.WHITE
            drawCircle(fretboard.win, note_colour, Colours.BLACK,(note_pos, centre_y), AM.NOTE_CIRCLE_RADIUS)

            if AM.SHOW_SCALE_NUMBERS and self.checkNoteHighlighted(note):
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
        if AM.ACTIVE_ROOT == None or AM.ACTIVE_SCALE == None:
            return False
        
        notes_in_scale = AM.getNotesInScale(AM.ACTIVE_ROOT, AM.ACTIVE_SCALE)
        
        if notes_in_scale.__contains__(note):
            note_index = notes_in_scale.index(note)
            note_colour = Colours.SCALE_NOTES_COLORS[note_index]
            return note_colour
        else:
            return False





class Fretboard():
    def __init__(self, win, zone_pos, zone_width, zone_height, neck_len, neck_width, bg_color, neck_colour):
        self.win = win
        self.zone_height = zone_height
        self.zone_width = zone_width
        self.neck_len = neck_len
        self.neck_width = neck_width
        self.bg_color = bg_color
        self.neck_colour = neck_colour        
        self.rect = pygame.Rect(zone_pos[0], zone_pos[1], zone_width, zone_height)

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

        for i, open_note in enumerate(AM.GUITAR_TUNING):
            self.all_strings.append(GuitarString(6 - i, open_note))
        
        tuning_sect_width = 800
        tuning_sect_height = 50
        tuning_sect_size = [tuning_sect_width, tuning_sect_height]
        tuning_sect_min_gap = 50
        tuning_sect_xPos = self.rect.centerx - tuning_sect_width/2 
        tuning_sect_yPos = self.rect.bottom - self.rect.height/16 * 3
        tuning_sect_pos = [tuning_sect_xPos, tuning_sect_yPos]
    
        self.tuning_settings = TuningSection(tuning_sect_pos,tuning_sect_size, tuning_sect_min_gap)

        # self.set_tunings = Set


    def drawFretboard(self):
        print(f"Note circle radius: {AM.NOTE_CIRCLE_RADIUS}")

        # Draw Background colour
        pygame.draw.rect(self.win, self.bg_color, (0,0,self.zone_width, self.zone_height))

        if AM.ACTIVE_ROOT and AM.ACTIVE_SCALE:
            # Title showing current root note and scale
            active_setup_text = f"{AM.ACTIVE_ROOT} {AM.ACTIVE_SCALE}"
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
            dot_y_pos = self.zone_height - self.y_padding + dist_above_neck
            if DOT_POSITIONS.__contains__(i+1):
                dot_pos = (fret_xPos + self.fret_spacing/2, dot_y_pos)
                print(dot_pos)
                pygame.draw.circle(self.win, Colours.BLACK, dot_pos, 3)

            elif DOUBLE_DOT_POSITIONS.__contains__(i+1):
                dot_1_pos = dot_pos = (fret_xPos + self.fret_spacing/3, dot_y_pos)
                dot_2_pos = dot_pos = (fret_xPos + self.fret_spacing*2/3, dot_y_pos)
                pygame.draw.circle(self.win, Colours.BLACK, dot_1_pos, 3)
                pygame.draw.circle(self.win, Colours.BLACK, dot_2_pos, 3)

        # Strings
        for string in self.all_strings:
            string.drawStringNotes(self)
        
        self.tuning_settings.DrawSection(self.win)

        # self.setTuningMenu.DrawSection(self.win)

    def checkMouseInput(self, mousePos):
        for tuning_box in self.tuning_settings.all_text_boxes:
            tuning_box.CheckArrowClicks(mousePos)


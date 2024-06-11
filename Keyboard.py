import pygame
from colours import Colours
from AppManager import ALL_NOTES
from AppManager import FONT
import AppManager
from button import Button

# SHARP_POSITIONS = [2,4,7,9,11,14,16,19,21,23] # from C to C
SHARP_POSITIONS = [2,3,5,6,7,9,10,12,13,14]
# ALL_NOTES = ['c','c#','d','d#','e','f','f#','g','g#','a','a#','b']

x_padding = 100
y_padding = 100

num_keys = 24

white_key_font = AppManager.getFont(40)
note_number_font = AppManager.getFont(30)

class Key():
    def __init__(self, id, note, isSharp):
        self.id = id
        self.note = note
        self.isSharp = isSharp
        self.isHighlighted = False
        self.num_in_scale = 0
    
    def createRect(self, xPos, yPos, keywidth, keyheight):
        self.rect = pygame.Rect(xPos, yPos, keywidth-2, keyheight)
    
    def drawKey(self, win):
        if self.isSharp:
            key_colour = Colours.GREEN if self.isHighlighted else Colours.BLACK
            pygame.draw.rect(win, key_colour, self.rect)
        else:
            key_colour = Colours.BLUE if self.isHighlighted else Colours.WHITE
            pygame.draw.rect(win, key_colour, self.rect)
            note_label = white_key_font.render(self.note, True, Colours.BLACK)
            note_label_size = white_key_font.size(self.note)
            note_label_pos = (self.rect.left + (self.rect.width - note_label_size[0])/2, self.rect.bottom - note_label_size[1]-20)
            win.blit(note_label, note_label_pos)

        if self.isHighlighted:
            note_number_radius = 13

            centre_pos = list(self.rect.center)
            centre_pos[1] += self.rect.height/4
            pygame.draw.circle(win, Colours.RED, centre_pos, note_number_radius)

            note_num = str(self.num_in_scale)
            note_number_text = note_number_font.render(note_num, True, Colours.WHITE)
            note_number_text_size = note_number_font.size(note_num)
            note_number_pos = (centre_pos[0] - note_number_text_size[0]/2, centre_pos[1] - note_number_text_size[1]/2)
            win.blit(note_number_text, note_number_pos)
            # Draw circle in centre of key with number in scale (self.num_in_scale)

        
            

class Keyboard():
    def __init__(self, win, zone_width, zone_height, bg_colour):
        self.win = win
        self.zone_width = zone_width
        self.zone_height = zone_height
        self.x_offset = x_padding
        self.y_offset = y_padding
        self.keywidth = round((zone_width - 2*x_padding) / 14)
        self.keyheight = round(zone_height-2*y_padding)
        self.bg_colour = bg_colour

        self.rect = pygame.Rect(0,0,self.zone_width, self.zone_height)

        self.all_keys = []

        self.createKeyboard()


    
    def createKeyboard(self):
        for i in range(num_keys):
            current_note = ALL_NOTES[i % len(ALL_NOTES)]
            isSharp = current_note.__contains__('#')
            self.all_keys.append(Key(i,current_note, isSharp))

        self.whites = [key for key in self.all_keys if not key.isSharp]
        self.blacks = [key for key in self.all_keys if key.isSharp]


        # Designate postions of all white and black keys
        for i, key in enumerate(self.whites):
            xPos = self.x_offset + i*self.keywidth
            yPos = self.y_offset
            key.createRect(xPos, yPos, self.keywidth, self.keyheight)
        
        for i, key in enumerate(self.blacks):
            black_keywidth = self.keywidth*0.6
            xPos = self.x_offset + self.keywidth*(SHARP_POSITIONS[i]-1) - black_keywidth/2
            key.createRect(xPos, yPos, black_keywidth, self.keyheight/2)

        clear_button_width = 90
        clear_button_height = 40
        clear_button_font = AppManager.getFont(30)
        clear_button_pos = (self.rect.bottomright[0] - clear_button_width - 10, self.rect.bottomright[1] - clear_button_height - 10)
        clear_button_rect = pygame.Rect(clear_button_pos[0], clear_button_pos[1], clear_button_width, clear_button_height)
        self.clear_button = Button(clear_button_rect, "Clear", clear_button_font, Colours.RED, Colours.RED, Colours.WHITE, None)
        


    def drawKeyboard(self):
        pygame.draw.rect(self.win,self.bg_colour, (0,0,self.zone_width, self.zone_height))

        if AppManager.ACTIVE_ROOT and AppManager.ACTIVE_SCALE:
            # Title showing current root note and scale
            active_setup_text = f"{AppManager.ACTIVE_ROOT} {AppManager.ACTIVE_SCALE}"
        else:
            active_setup_text = "No Scale Selected"
        text = FONT.render(active_setup_text, True, Colours.WHITE)

        font_size = FONT.size(active_setup_text)
        title_pos = ((self.zone_width - font_size[0])/2, (y_padding - font_size[1])/2)
        self.win.blit(text, title_pos)

        for key in self.whites:
            key.drawKey(self.win)
        for key in self.blacks:
            key.drawKey(self.win)
        
        # Draw Clear Button
        self.clear_button.update(self.win)

        pygame.display.update()
    
    def updateKeyboard(self):
        if AppManager.ACTIVE_ROOT == None or AppManager.ACTIVE_SCALE == None:
            for key in self.all_keys:
                key.isHighlighted = False
            
            self.drawKeyboard()
            return
        notes_in_scale = AppManager.getNotesInScale(AppManager.ACTIVE_ROOT, AppManager.ACTIVE_SCALE)
        for key in self.all_keys:
            if notes_in_scale.__contains__(key.note):
                key.isHighlighted = True
                key.num_in_scale = notes_in_scale.index(key.note)+1
                # print(f"Note {key.note} :: {key.num_in_scale}")
            else:
                key.isHighlighted = False

        self.drawKeyboard()
    
    def checkClearPressed(self, mouse_pos):
        if self.clear_button.checkForInput(mouse_pos):
            AppManager.ACTIVE_ROOT = None
            AppManager.ACTIVE_SCALE = None
            return True
    
        return False
            

          



            
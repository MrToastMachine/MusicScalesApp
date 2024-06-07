import pygame
from colours import Colours

# SHARP_POSITIONS = [2,4,7,9,11,14,16,19,21,23] # from C to C
SHARP_POSITIONS = [2,3,5,6,7,9,10,12,13,14]
ALL_NOTES = ['c','c#','d','d#','e','f','f#','g','g#','a','a#','b']

x_padding = 100
y_padding = 100

num_keys = 24

class Key():
    def __init__(self, id, note, isSharp):
        self.id = id
        self.note = note
        self.isSharp = isSharp
    
    def createRect(self, xPos, yPos, keywidth, keyheight):
        self.rect = (xPos, yPos, keywidth-2, keyheight)
    
    def drawKey(self, win):
        key_colour = Colours.BLACK if self.isSharp else Colours.WHITE
        pygame.draw.rect(win, key_colour, self.rect)

class Keyboard():
    def __init__(self, zone_width, zone_height, bg_colour):
        self.zone_width = zone_width
        self.zone_height = zone_height
        self.x_offset = x_padding
        self.y_offset = y_padding
        self.keywidth = round((zone_width - 2*x_padding) / 14)
        self.keyheight = round(zone_height-2*y_padding)
        self.bg_colour = bg_colour

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


    def drawKeyboard(self, win):
        pygame.draw.rect(win,self.bg_colour, (0,0,self.zone_width, self.zone_height))
        for key in self.whites:
            key.drawKey(win)
        for key in self.blacks:
            key.drawKey(win)
        
        pygame.display.update()
    
    def newScale(self, rootnote, scale):
        pass
        # update which keys are highlighted
        # pull from scales storage
        # Call the draw keyboard function


          



            
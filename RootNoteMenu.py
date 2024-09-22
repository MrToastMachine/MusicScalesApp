import pygame
from button import Button
from AppManager import ALL_NOTES
from AppManager import FONT
import AppManager
from colours import Colours

padding = 50

sect_pad = AppManager.SECTION_PADDING

class RootNoteMenu():
    def __init__(self, pos, dimensions, button_size, bg_col, butt_colour, butt_colour_highlighted):
        
        self.xPos, self.yPos = pos
        self.width, self.height = dimensions
        self.button_size = button_size

        if self.width < self.height:
            self.VERTICAL = True
    
        self.button_area_width = self.width - 2*padding
        self.button_gap = (self.button_area_width - 12*self.button_size)/11
        self.all_buttons = []

        self.padding = padding
        self.y_padding = (self.height - self.button_size) / 2 

        self.bg_colour = bg_col
        self.butt_colour = butt_colour
        self.butt_colour_highlighted = butt_colour_highlighted

        self.createMenu()

    # Designate positions of all buttons
    # Called once at instantiation
    def createMenu(self):
        self.rect = (self.xPos + sect_pad/2, self.yPos + sect_pad/2, self.width - sect_pad, self.height - sect_pad)
        for i, note in enumerate(ALL_NOTES):
            xStart = self.padding + i*(self.button_size + self.button_gap)
            yStart = self.y_padding + self.yPos

            rect = pygame.Rect(xStart, yStart, self.button_size, self.button_size)

            button = Button(rect,note, FONT, self.butt_colour, Colours.BLACK, None)

            self.all_buttons.append(button)

    def drawMenu(self, screen):
        pygame.draw.rect(screen, self.bg_colour, self.rect, border_radius=AppManager.SECTION_CORNER_RADIUS)
        for butt in self.all_buttons:
            if butt.text_input == AppManager.ACTIVE_ROOT:
                butt.base_colour = self.butt_colour_highlighted
            else:
                butt.base_colour = self.butt_colour
                
            butt.update(screen)

    def checkAllButtonsForInput(self, mousePos):
        for butt in self.all_buttons:
            if butt.checkForInput(mousePos):
                AppManager.ACTIVE_ROOT = butt.text_input
                print(butt.text_input)
                return True
                

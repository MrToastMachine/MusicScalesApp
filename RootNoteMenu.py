import pygame
from button import Button
from AppManager import ALL_NOTES
from AppManager import FONT
import AppManager
from colours import Colours

PADDING = 50

SECT_PADDING = AppManager.SECTION_PADDING

class RootNoteMenu():
    def __init__(self, pos, dimensions, button_size, bg_col, butt_colour, butt_colour_highlighted, is_vertical):
        
        self.xPos, self.yPos = pos
        self.width, self.height = dimensions
        self.button_size = button_size
        self.is_vertical = is_vertical
    
        self.button_area_width = self.width - 2*PADDING
        self.button_area_height = self.height - 2*PADDING

        self.all_buttons = []

        self.padding = PADDING
        self.y_padding = (self.height - self.button_size) / 2 

        self.bg_colour = bg_col
        self.butt_colour = butt_colour
        self.butt_colour_highlighted = butt_colour_highlighted

        if self.is_vertical:
            self.createVerticalMenu()
        else:
            self.createHorizontalMenu()

    # Designate positions of all buttons
    # Called once at instantiation
    def createHorizontalMenu(self):
        self.button_gap = (self.button_area_width - 12*self.button_size)/11

        #button_area
        self.rect = (self.xPos + SECT_PADDING/2, self.yPos + SECT_PADDING/2, self.width - SECT_PADDING, self.height - SECT_PADDING)
        for i, note in enumerate(ALL_NOTES):
            xStart = self.padding + i*(self.button_size + self.button_gap)
            yStart = self.y_padding + self.yPos

            rect = pygame.Rect(xStart, yStart, self.button_size, self.button_size)

            button = Button(rect,note, FONT, self.butt_colour, Colours.BLACK, None)

            self.all_buttons.append(button)

    def createVerticalMenu(self):
        self.button_gap = (self.button_area_height - 12*self.button_size)/11

        self.rect = (self.xPos + SECT_PADDING/2, self.yPos + SECT_PADDING/2, self.width - SECT_PADDING, self.height - SECT_PADDING)
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
                

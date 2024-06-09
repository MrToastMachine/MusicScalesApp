import pygame
from button import Button
from AppManager import ALL_NOTES
from AppManager import FONT
import AppManager
from colours import Colours

x_padding = 50

class RootNoteMenu():
    def __init__(self, pos, dimensions, button_size):
        self.xPos, self.yPos = pos
        self.width, self.height = dimensions
        self.button_size = button_size
        
        self.button_area_width = self.width - 2*x_padding
        self.button_gap = (self.button_area_width - 12*self.button_size)/11
        self.all_buttons = []

        self.x_padding = x_padding
        self.y_padding = (self.height - self.button_size) / 2 

        self.createMenu()

    # Designate positions of all buttons
    # Called once at instantiation
    def createMenu(self):
        for i, note in enumerate(ALL_NOTES):
            xStart = self.x_padding + i*(self.button_size + self.button_gap)
            yStart = self.y_padding + self.yPos

            rect = pygame.Rect(xStart, yStart, self.button_size, self.button_size)

            button = Button(rect,note, FONT, Colours.GREEN, Colours.GREEN, Colours.BLACK, None)

            self.all_buttons.append(button)

    def drawMenu(self, screen):
        pygame.draw.rect(screen, Colours.WHITE, (self.xPos, self.yPos, self.width, self.height))
        for butt in self.all_buttons:
            butt.update(screen)

    def checkAllButtonsForInput(self, mousePos):
        for butt in self.all_buttons:
            if butt.checkForInput(mousePos):
                AppManager.ACTIVE_ROOT = butt.text_input
                print(butt.text_input)
                return True
                

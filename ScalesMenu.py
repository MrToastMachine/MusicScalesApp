import pygame
from button import Button
from AppManager import ALL_NOTES
from AppManager import FONT
import AppManager
from colours import Colours

x_padding = 50
y_padding = 50

sect_pad = AppManager.SECTION_PADDING


class ScalesMenu():
    def __init__(self, pos, dimensions, button_height, bg_colour, butt_colour, butt_colour_highlighted):
        self.xPos, self.yPos = pos
        self.width, self.height = dimensions
        self.button_height = button_height
        
        self.button_area_height = self.height - 2*y_padding
        self.button_width = self.width - 2*x_padding

        num_buttons = len(AppManager.scales)
        self.button_gap = (self.button_area_height - num_buttons*self.button_height)/(num_buttons-1)
        self.all_buttons = []

        self.x_padding = x_padding
        self.y_padding = y_padding

        self.bg_colour = bg_colour
        self.butt_colour = butt_colour
        self.butt_colour_highlighted = butt_colour_highlighted

        self.createMenu()

    # Designate positions of all buttons
    # Called once at instantiation
    def createMenu(self):
        self.rect = (self.xPos + sect_pad/2, self.yPos + sect_pad/2, self.width - sect_pad, self.height - sect_pad)
        for i, note in enumerate(AppManager.scales):
            xStart = self.xPos + self.x_padding
            yStart = self.y_padding + self.yPos + i*(self.button_height + self.button_gap)

            rect = pygame.Rect(xStart, yStart, self.button_width, self.button_height)

            button = Button(rect, note, FONT, self.butt_colour, Colours.BLACK, None)

            self.all_buttons.append(button)

    def drawMenu(self, screen):
        pygame.draw.rect(screen, self.bg_colour, self.rect, border_radius=AppManager.SECTION_CORNER_RADIUS)
        for butt in self.all_buttons:
            if butt.text_input == AppManager.ACTIVE_SCALE:
                butt.base_colour = self.butt_colour_highlighted
            else:
                butt.base_colour = self.butt_colour

            butt.update(screen)

    def checkAllButtonsForInput(self, mousePos):
        for butt in self.all_buttons:
            if butt.checkForInput(mousePos):
                AppManager.ACTIVE_SCALE = butt.text_input
                print(butt.text_input)
                return True
            
    

                

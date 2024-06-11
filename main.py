import pygame
from Keyboard import Keyboard
from RootNoteMenu import RootNoteMenu
from ScalesMenu import ScalesMenu
from colours import Colours
from button import Button
import AppManager
from AppManager import ALL_NOTES
from AppManager import FONT

import time

pygame.init()
AppManager.readInScales()


FPS = 60
RES = (1400, 700)
# RES = (1400, 700)
win = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

keyb = Keyboard(win, 1000, 600, Colours.GRAY)
keyb.drawKeyboard()


button_size = 50

root_menu = RootNoteMenu((0,600),(1000, 100),button_size)
root_menu.drawMenu(win)

scales_menu = ScalesMenu((1000,0), (400,700), 40)
scales_menu.drawMenu(win)
pygame.display.update()

running = True
while(running):
    clock.tick(FPS)
    mouse_pos = pygame.mouse.get_pos()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if (root_menu.checkAllButtonsForInput(mouse_pos)):
                keyb.updateKeyboard()
            elif (scales_menu.checkAllButtonsForInput(mouse_pos)):
                keyb.updateKeyboard()
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # keyb.newScale('c', srcs.scales['Blues'])
                print("[[[ SPACEBAR ]]]")

        pygame.display.update()
    # drawFrame()

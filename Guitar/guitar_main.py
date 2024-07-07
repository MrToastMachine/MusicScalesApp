import pygame
from Fretboard import Fretboard
from RootNoteMenu import RootNoteMenu
from ScalesMenu import ScalesMenu
from colours import Colours
from button import Button
import AppManager
from AppManager import ALL_NOTES
from AppManager import FONT

pygame.init()
AppManager.readInScales()

FPS = 60
RES = (1000, 600)
# RES = (1400, 700)
win = pygame.display.set_mode(RES)
clock = pygame.time.Clock()


win.fill(Colours.BACKGROUND_COLOR)


fretboard = Fretboard(win, 1000, 600, Colours.KEYB_BG_COLOR)
fretboard.drawFretboard()


running = True
while(running):
    clock.tick(FPS)
    mouse_pos = pygame.mouse.get_pos()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # if (fret.checkAllButtonsForInput(mouse_pos)):
            #     keyb.updateKeyboard()
            # elif (scales_menu.checkAllButtonsForInput(mouse_pos)):
            #     keyb.updateKeyboard()
            # elif (keyb.checkClearPressed(mouse_pos)):
            #     keyb.updateKeyboard()
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # keyb.newScale('c', srcs.scales['Blues'])
                print("[[[ SPACEBAR ]]]")
                # keyb.clearKeyboard()

        pygame.display.update()
    # drawFrame()

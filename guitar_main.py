# TODO: https://www.scales-chords.com/scalefinder.php

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
# RES = (1000, 600)
RES = (1600, 900)
win = pygame.display.set_mode(RES)
clock = pygame.time.Clock()


win.fill(Colours.BACKGROUND_COLOR)

# TODO: Make section in code for all static size variables 
ROOT_NOTE_BUTTON_SIZE = 50

# TODO: Pass in rects for each section instead of position and size -> neater

FRETBOARD_AREA = pygame.Rect(0,0, 1200, 600)
ROOT_NOTE_AREA = pygame.Rect(0,800, 1200, 100)
SCALE_AREA = pygame.Rect(1200, 0, 400, 900)
TUNING_MENU_AREA = pygame.Rect(0,600,1200,200)
NECK_LEN = round(FRETBOARD_AREA.width * 0.8)

fretboard = Fretboard(win, FRETBOARD_AREA.topleft, FRETBOARD_AREA.width, FRETBOARD_AREA.height, NECK_LEN, 200, Colours.KEYB_BG_COLOR, Colours.BROWN)
fretboard.drawFretboard()


root_menu = RootNoteMenu(ROOT_NOTE_AREA.topleft, (ROOT_NOTE_AREA.width, ROOT_NOTE_AREA.height), ROOT_NOTE_BUTTON_SIZE, Colours.RNM_BG_COLOR, Colours.BUTTON_COLOR, Colours.BUTTON_COLOR_HIGHLIGHTED, False)
root_menu.drawMenu(win)

# tuning_menu = TuningMenu()
pygame.draw.rect(win, Colours.BONE, TUNING_MENU_AREA, border_radius=10)

scales_menu = ScalesMenu(SCALE_AREA.topleft, (SCALE_AREA.width, SCALE_AREA.height), 40, Colours.SCALES_BG_COLOR, Colours.BUTTON_COLOR, Colours.BUTTON_COLOR_HIGHLIGHTED)
scales_menu.drawMenu(win)
pygame.display.update()

def drawFrame():
    fretboard.drawFretboard()
    root_menu.drawMenu(win)
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
                fretboard.drawFretboard()
                print(f"[ROOT NOTE UPDATE]  -->  [{AppManager.ACTIVE_ROOT}]")
            elif (scales_menu.checkAllButtonsForInput(mouse_pos)):
                fretboard.drawFretboard()
                print(f"[SCALE UPDATE]  -->  [{AppManager.ACTIVE_SCALE}]")
            elif (fretboard.checkMouseInput(mouse_pos)):
                fretboard.drawFretboard()
                print("Something on fretboard section clicked")
                



            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # keyb.newScale('c', srcs.scales['Blues'])
                print("[[[ SPACEBAR ]]]")
                AppManager.toggleScaleNumbers()
                # keyb.clearKeyboard()
            elif event.key == pygame.K_DOWN:
                print("DOWN DOWN DOWN")
                AppManager.NOTE_CIRCLE_RADIUS -= 1
            elif event.key == pygame.K_UP:
                print("UP UP UP")
                AppManager.NOTE_CIRCLE_RADIUS += 1
            
        else:
            continue

        print("[ALERT] Something triggered!")
        drawFrame()
        

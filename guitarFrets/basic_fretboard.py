import pygame
from button_pkg import *
import json

pygame.init()

RES = (1200, 400)
FPS = 5

win = pygame.display.set_mode(RES)
clk = pygame.time.Clock()

BG_COLOR = (200,200,180)
BROWN = (50,30,20)
WHITE = (255,255,255)
GRAY = (150,150,150)
BLACK = (0,0,0)
RED = (255,0,0)

neckLen = 1000
numFrets = 24
fretSize = round(neckLen/numFrets)

font = pygame.font.SysFont(None, 24)

def drawFretboard():
    for i in range(numFrets):
        fretThickness = 4
        x = i * fretSize + 100
        pygame.draw.line(win, GRAY, [x, 100], [x,300], fretThickness)
        
        fretNumTxt = font.render(str(i),True, BROWN)
        win.blit(fretNumTxt, (x+5, 305))

def drawStrings():
    for i in range(6):
        y = RES[1] - (128 + i*29)
        pygame.draw.line(win, WHITE, [100,y], [1100,y], 2)


def drawFrame():
    win.fill(BG_COLOR)
    pygame.draw.rect(win, BROWN, (100,100,neckLen, 200))

    drawFretboard()
    drawStrings()
    Button_Circle.drawButtons()

    pygame.display.update()

def initialization():
    for i in range(numFrets-1):
        x = 100 + (i*fretSize + fretSize/2)
        y = RES[1] - 128
        Button_Circle(win, x, y, 8, RED, str(i))

    # def __init__(self, win, xPos, yPos, radius, color, text):

initialization()

run = True
while run:
    clk.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            Button_Circle.check_if_clicked(mousePos)
        
    drawFrame()

pygame.quit()
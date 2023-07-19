# This file generates accurate fret spacings
# Kind of overcomplicates the task I'm trying to achieve
# -----> NOT WORTH IT

import pygame
pygame.init()

RES = (1200, 400)
FPS = 1

win = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

bg_color = (200,200,180)
brown = (50,30,20)
white = (255,255,255)
gray = (150,150,150)
black = (0,0,0)
red = (255,0,0)

neckLen = 1200
fretDists = [0]
numFrets = 23
distScale = 1

font = pygame.font.SysFont(None, 24)

for i in range(1,numFrets):
    dist = (neckLen*1.4-fretDists[i-1])/20 + fretDists[i-1]
    fretDists.append(round(dist))


def drawFrets():
    fretNum = 1
    for fret in fretDists[:-1]:
        thickness = 4
        x = (fret * distScale) - thickness/2
        pygame.draw.line(win, gray, [x,100], [x,300], thickness)


        fretNumTxt = font.render(str(fretNum),True, brown)
        win.blit(fretNumTxt, (x+5, 305))
        fretNum += 1

def drawStrings():
    for i in range(6):
        y = RES[1] - (128 + i*29)
        pygame.draw.line(win, white, [0,y], [1200,y], 2)

        for j in range(numFrets-1):
            rad = 8
            notePos = (fretDists[j+1]+fretDists[j])/2
            pygame.draw.circle(win, red, [notePos,y], rad)


def drawFrame():
    win.fill(bg_color)
    pygame.draw.rect(win, brown, (0,100,1200,200))
    
    drawFrets()
    drawStrings()

    pygame.display.update()

run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    drawFrame()


pygame.quit()
import pygame
from Keyboard import Keyboard
from colours import Colours

pygame.init()

FPS = 30
RES = (1000, 800)
clock = pygame.time.Clock()
win = pygame.display.set_mode(RES)

keyb = Keyboard(800,400,Colours.GRAY)
keyb.drawKeyboard(win)

running = True
while(running):
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # drawFrame()

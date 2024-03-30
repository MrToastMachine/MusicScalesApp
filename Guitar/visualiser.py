import pygame
pygame.init()

RES = (1300, 300)
FPS = 10

window = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

#COLOURS
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

def update():
	pass

run = True
while run:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	update()
	pygame.display.update()

pygame.quit()
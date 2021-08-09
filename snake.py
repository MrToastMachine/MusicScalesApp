import pygame
import random
import time
pygame.init()

RES = (320,350)
FPS = (10)

window = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
pygame.display.set_caption("Snake... Snaaaaaake")

#Colours
white = (255,255,255)
cream = (255,255,210)
black = (0,0,10)
yellow = (255,255,0)
green = (100,255,100)
red = (180,30,30)

blockSize = 10
gridPos = [10,10]
gridWidth = 30
gridHeight = 30

class Player():
	bodyParts = []

	def __init__(self,pos=[0,0]):
		self.pos = pos
		self.x = gridPos[0] + (pos[0]*blockSize)
		self.y = gridPos[1] + (pos[1]*blockSize)
		self.length = 1
		Player.bodyParts.append(pos)
		for i in range(1,3):
			Player.bodyParts.append([pos[0]-i,pos[1]])
		self.eaten = False

	def drawPlayer(self):
		for i in range(len(Player.bodyParts)):
			xPos = gridPos[0] + (Player.bodyParts[i][0] * blockSize)
			yPos = gridPos[1] + (Player.bodyParts[i][1] * blockSize)
			pygame.draw.rect(window, black, (xPos, yPos, 9, 9))

	def movePlayer(self, direction):
		length = len(Player.bodyParts)
		tailPos = [Player.bodyParts[length-1][0],Player.bodyParts[length-1][1]]
		for i in range(1,length):
			for j in range(2):
				Player.bodyParts[length-i][j] = Player.bodyParts[length-i-1][j]
		if(direction == "left"):
			Player.bodyParts[0][0] -= 1
		elif(direction == "right"):
			Player.bodyParts[0][0] += 1
		elif(direction == "up"):
			Player.bodyParts[0][1] -= 1
		elif(direction == "down"):
			Player.bodyParts[0][1] += 1
		else:		  	
			print("Error Occured when moving")
		if(self.eaten):
			Player.bodyParts.append(tailPos)
			self.eaten = False

class Food():
	def __init__(self):
		self.getPos()

	def getPos(self):
		self.pos = [random.randint(0,29),random.randint(0,29)]
		self.x = gridPos[0] + (blockSize*self.pos[0])
		self.y = gridPos[1] + (blockSize*self.pos[1])
		

def drawFrame():
	window.fill(black)
	pygame.draw.rect(window, cream, (gridPos[0]-1,gridPos[1]-1,301,301))

	pygame.draw.rect(window, red, (food.x, food.y, 9, 9))
	try:
		snake.drawPlayer()
	except:
		endgame = font.render("You Lose!", 1, black)
		window.blit(endgame,(110, 150))

	scoreText = font.render("Score: " + str(score), 1, white)
	window.blit(scoreText, (10, gridPos[1]+(gridHeight*blockSize)+5))
	pygame.display.update()


score = 0
moveDir = "right"
font = pygame.font.SysFont('corbel', 25, True)
snake = Player([15,15])
food = Food()
running = True
while(running):
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False


	keyPressed = pygame.key.get_pressed()

	if((keyPressed[pygame.K_UP] or keyPressed[pygame.K_w]) and Player.bodyParts[0][1] > 0 and moveDir != "down"):
		moveDir = "up"
	elif((keyPressed[pygame.K_DOWN] or keyPressed[pygame.K_s]) and Player.bodyParts[0][1] < gridHeight-1 and moveDir != "up"):
		moveDir = "down"
	elif((keyPressed[pygame.K_LEFT] or keyPressed[pygame.K_a]) and Player.bodyParts[0][0] > 0 and moveDir != "right"):
		moveDir = "left"
	elif((keyPressed[pygame.K_RIGHT] or keyPressed[pygame.K_d]) and Player.bodyParts[0][0] < gridWidth-1 and moveDir != "left"):
		moveDir = "right"

	snake.movePlayer(moveDir)

	if Player.bodyParts[0] == food.pos:
		score += 1
		food.getPos()
		snake.eaten = True
		# FPS += 1
	elif (not 0 <= Player.bodyParts[0][0] <= 29) or (not 0 <= Player.bodyParts[0][1] <= 29) or (Player.bodyParts.count(Player.bodyParts[0])>1):
		print("Outside")
		del(snake)
		running = False
	drawFrame()

time.sleep(3)
pygame.quit()

# for i in range(gridWidth):
# 	for j in range(gridHeight):
# 		xPos = gridPos[0]+(i*blockSize)
# 		yPos = gridPos[1]+(j*blockSize)
# 		pygame.draw.rect(window, black, (xPos,yPos, 9, 9))
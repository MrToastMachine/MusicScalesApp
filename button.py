import pygame
import AppManager

class Button():
	all_buttons = []

	def __init__(self, rect, text_input, font, base_color, hovering_color, text_color, command):
		self.rect = rect
		# self.x_pos = pos[0]
		# self.y_pos = pos[1]
		# self.width, self.height = size
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text_color = text_color
		self.text = self.font.render(self.text_input, True, self.text_color)
		self.image = self.text
		# self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
		# self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

		self.command = command

		Button.all_buttons.append(self)

	def update(self, screen):
		pygame.draw.rect(screen, self.base_color, self.rect)

		# Get size of text in order to center it correctly in button
		text_size = self.font.size(self.text_input)
		text_pos_x = self.rect.center[0] - text_size[0]/2
		text_pos_y = self.rect.center[1] - text_size[1]/2

		screen.blit(self.text, (text_pos_x, text_pos_y))

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)


				
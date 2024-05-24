import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1500, 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

all_notes = ['a','a#','b','c','c#','d','d#','e','f','f#','g','g#']

# Fonts
FONT = pygame.font.SysFont(None, 50)

# Dropdown options
scales = {
    "Major": [1, 3, 5, 6, 8, 10, 12],
    "Minor": [1, 3, 4, 6, 8, 9, 11],
    "Pentatonic Major": [1, 3, 5, 8, 10],
    "Pentatonic Minor": [1, 4, 6, 8, 11],
    "Blues": [1, 4, 6, 7, 8, 11],
    "Harmonic Minor": [1, 3, 4, 6, 8, 9, 12],
    "Melodic Minor": [1, 3, 4, 6, 8, 10, 12],
    "Dorian": [1, 3, 4, 6, 8, 10, 11],
    "Mixolydian": [1, 3, 5, 6, 8, 10, 11]
}

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dropdown Menu Example")

# Dropdown variables
dropdown_open = False
selected_scale = None
options_rect = pygame.Rect(100, 50, 200, 30)
option_height = 30

button_size = 50
x_padding = 50
button_area_width = WIDTH - 2*x_padding
gap = (button_area_width - 12*button_size)/(11)

def drawFrame():
    screen.fill(BLACK)

    y_height = HEIGHT/2 - button_size/2
    for i, note in enumerate(all_notes):
        xStart = x_padding + i*(button_size+gap)

        rect = pygame.Rect(xStart, y_height, button_size, button_size)
        pygame.draw.rect(screen, GRAY, rect)

        note_text = FONT.render(note,1,BLACK)
        screen.blit(note_text, (xStart + button_size/8, y_height + button_size/8))
    
    pygame.display.update()

drawFrame()

# Main loop
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if options_rect.collidepoint(event.pos):
                dropdown_open = not dropdown_open
            elif dropdown_open:
                for i, scale in enumerate(scales.keys()):
                    option_rect = pygame.Rect(100, 50 + (i + 1) * option_height, 200, option_height)
                    if option_rect.collidepoint(event.pos):
                        selected_scale = scale
                        dropdown_open = False
                        break
            else:
                dropdown_open = False


pygame.quit()
sys.exit()

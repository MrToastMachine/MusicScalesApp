import pygame

class GuitarString():
    def __init__(self, str_num, open_note):
        self.str_num = str_num

class Fretboard():
    def __init__(self, win, zone_width, zone_height, bg_color):
        self.win = win
        self.zone_height = zone_height
        self.zone_width = zone_width
        # self.x_offset = x_padding
        # self.y_offset = y_padding

    def createFretboard(self):
        self.rect = pygame.Rect()

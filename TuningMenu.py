import pygame

class TuningMenu():
    def __init__(self, rect, butt_colour, text_colour, num_rows=3, num_cols=4):
        self.rect = rect
        self.butt_colour = butt_colour
        self.text_colour = text_colour
        self.num_rows = num_rows
        self.num_cols = num_cols

    def createMenu(self):
        for 
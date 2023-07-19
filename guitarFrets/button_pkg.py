import math
import pygame

class Button_Circle():
    button_circle_list = []
    
    def __init__(self, win, xPos, yPos, radius, color, text=""):
        self.win = win
        self.xPos = xPos
        self.yPos = yPos
        self.radius = radius
        self.color = color
        self.text = text
        Button_Circle.button_circle_list.append(self)
        print(f"New Button Created: {text}")
    
    @classmethod
    def check_if_clicked(cls, mouse_pos):
        for butt in cls.button_circle_list:
            if calc_dist(mouse_pos, (butt.xPos, butt.yPos)) <= butt.radius:
                print(f"[BUTTON CLICK] Button ID {butt.text}")
                return butt

    @classmethod
    def drawButtons(cls):
        for butt in cls.button_circle_list:
            pygame.draw.circle(butt.win, butt.color, [butt.xPos, butt.yPos], butt.radius)

def calc_dist(pointA, pointB):
    return math.sqrt((pointA[0]-pointB[0])**2 + (pointA[1]-pointB[1])**2)

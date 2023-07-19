import pygame
import json
from backendStructure import *
from keyboardVisualiser import *
import tkSettingsWindow as setting

class MainFrame():
    def __init__(self, win, myFont):
        self.ROOT_NOTE = "C"
        self.SCALE = "Major"
        self.keyboard = Keyboard(win, myFont)
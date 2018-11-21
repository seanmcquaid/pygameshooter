import pygame

class Hero(object):
    # classses always contain 2 parts
    # 1. the init = runs only once
    # 2. the methods = run whenever you call them
    def __init__ (self):
        self.x = 100
        self.y = 100
        self.speed = 10
        self.shouldMoveUp = False
        self.shouldMoveDown = False
        self.shouldMoveRight = False
        self.shouldMoveLeft = False
    def shouldMove(self, direction, start = True):
        if(direction == "up"):
            self.shouldMoveUp = start
        if(direction == "down"):
            self.shouldMoveDown = start
        if(direction == "right"):
            self.shouldMoveRight = start
        if(direction == "left"):
            self.shouldMoveLeft = start
    def drawMe(self):
        if (self.shouldMoveUp):
            self.y -= self.speed
        if (self.shouldMoveDown):
            self.y += self.speed
        if (self.shouldMoveRight):
            self.x += self.speed
        if (self.shouldMoveLeft):
            self.x -= self.speed
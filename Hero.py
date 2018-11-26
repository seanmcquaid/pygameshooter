import pygame
from pygame.sprite import Sprite

class Hero(Sprite):
    # classses always contain 2 parts
    # 1. the init = runs only once
    # 2. the methods = run whenever you call them
    def __init__ (self):
        super(Hero, self).__init__()
        self.x = 100
        self.y = 100
        self.speed = 5
        self.shouldMoveUp = False
        self.shouldMoveDown = False
        self.shouldMoveRight = False
        self.shouldMoveLeft = False
        self.rect = pygame.Rect(0, 0, 64, 64)
        self.rect.centerx = self.x
        self.rect.centery = self.y
    def shouldMove(self, direction, start = True):
        if(direction == "up"):
            self.shouldMoveUp = start
        if(direction == "down"):
            self.shouldMoveDown = start
        if(direction == "right"):
            self.shouldMoveRight = start
        if(direction == "left"):
            self.shouldMoveLeft = start
    def drawMe(self, w, h):
        self.w = w
        self.h = h 
        if (self.shouldMoveUp):
            if self.y > 32:
                self.y -= self.speed
                self.rect.y = self.y
        if (self.shouldMoveDown):
            if self.y <= h - 64:
                self.y += self.speed
                self.rect.y = self.y
        if (self.shouldMoveRight):
            if self.x <= w - 64:
                self.x += self.speed
                self.rect.x = self.x
        if (self.shouldMoveLeft):
            if self.x >= 32:
                self.x -= self.speed
                self.rect.x = self.x
from math import hypot
from pygame.sprite import Sprite
import pygame

#need pygame for rect

class BadGuy(Sprite):
    def __init__(self):
        super(BadGuy, self).__init__()
        self.x = 200
        self.y = 200
        self.speed = 2
        self.rect = pygame.Rect(0, 0, 32, 32)
        self.rect.centerx = self.x
        self.rect.centery = self.y
    def update_me(self, theHero):
        # find hypotonuse of triangle between hero and bad guy
        dx = self.x - theHero.x
        dy = self.y - theHero.y
        dist = hypot(dx,dy)
        dx = dx/dist
        dy = dy/dist
        self.x -= dx * self.speed
        self.y -= dy * self.speed
        # rectangle moves around with bad guy, if two rectangles collide
        self.rect.x = self.x
        self.rect.y = self.y
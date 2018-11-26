from pygame.sprite import Sprite
import pygame
# Sprite is a class
# sprite is the super class
# Arrow is the sub class

class Arrow(Sprite):
    def __init__(self, theHero):
        # must init a super class with subclass
        super(Arrow,self).__init__()
        self.x = theHero.x
        self.y = theHero.y
        self.speed = 20
        # rect is used in both arrow and badguy to enable collision
        # rectangles colliding
        self.rect = pygame.Rect(0, 0, 32, 32)
        self.rect.centerx = self.x
        self.rect.centery = self.y
    def updateMe(self):
        self.x += self.speed
        self.rect.x = self.x
        
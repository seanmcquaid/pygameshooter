from pygame.sprite import Sprite
import pygame
# Sprite is a class
# sprite is the super class
# Arrow is the sub class

class Arrow(Sprite):
    def __init__(self, theHero):
        # must init a super class with subclass
        super(Arrow,self).__init__()
        self.x = theHero.x + 10
        self.y = theHero.y + 10
        self.speed = 20
        # rect is used in both arrow and badguy to enable collision
        # rectangles colliding
        self.rect = pygame.Rect(0, 0, 32, 32)
        self.rect.centerx = self.x
        self.rect.centery = self.y
        self.arrows = []
        self.arrows.append(pygame.image.load('arrow1.png'))
        self.arrows.append(pygame.image.load('arrow2.png'))
        self.arrows.append(pygame.image.load('arrow3.png'))
        self.arrows.append(pygame.image.load('arrow4.png'))
        self.img = self.arrows[0]
        self.cur_arrow = 0
    def updateMe(self):
        self.cur_arrow += 1
        if self.cur_arrow == 4:
            self.cur_arrow = 0
        self.img = self.arrows[self.cur_arrow]
        self.x += self.speed
        self.rect.x = self.x
        self.rect.y = self.y
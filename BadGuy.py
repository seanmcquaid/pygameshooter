from math import hypot

class BadGuy(object):
    def __init__(self):
        self.x = 200
        self.y = 200
        self.speed = 4
    def update_me(self, theHero):
        # find hypotonuse of triangle between hero and bad guy
        dx = self.x - theHero.x
        dy = self.y - theHero.y
        dist = hypot(dx,dy)
        dx = dx/dist
        dy = dy/dist
        self.x -= dx * self.speed
        self.y -= dy * self.speed
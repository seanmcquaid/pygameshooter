import pygame.font

class Start_Button(object):
    def __init__(self, screen):
        self.screen = screen
        # how big is the screen?
        self.screen_rect = self.screen.get_rect()
        # set dimensions of the button image
        self.width = 250
        self.height = 100
        # set some colors
        self.button_color = 0,200,150
        self.text_color = 255,255,255 
        # get font from pygame
        self.font = pygame.font.Font(None, 52)
        # set the rect of the button
        self.rect = pygame.Rect(0,0,self.width,self.height)
        # set to center of the screen
        self.rect.center = self.screen_rect.center
    def setup_message(self):
        # play = text , True = anti alias to appear smoother, background = color 
        self.image_message = self.font.render("Play", True, self.text_color)
        self.image_message_rect = self.image_message.get_rect()
        self.image_message_rect.center = self.rect.center
    def draw_button(self):
        # fill in the button
        self.screen.fill(self.button_color, self.rect)
        #draw the button
        self.screen.blit(self.image_message,self.image_message_rect)
# miniconda access to run pygame
# cd ~/miniconda3/bin
# source activate py3k
# cd ~/development/11:18\ -\ Immersive/unit1/pygame_shooter
# python game.py

# 1. include pygame 
import pygame
import time
import random
from Hero import Hero
from BadGuy import BadGuy
from Arrow import Arrow
# Get group and groupcollide from the sprite module
from pygame.sprite import Group, groupcollide

# 2. initialize pygame
pygame.init()

# 3. make a screen with a size. The size MUST be a tuple
# made screen size equal to background image size
screen_size = (512, 480)
pygame_screen = pygame.display.set_mode(screen_size)

# 4. set the title of the window that opens
pygame.display.set_caption('Shooter')

#objects for each our hero and badguy
theHero = Hero()
hero = Group()
hero.add(theHero)


badGuy = BadGuy()
badGuys = Group()
badGuys.add(badGuy)

arrows = Group()

# ==========VARIABLES FOR OUR GAME ===============
#intro screen
white = (255,255,255)
clock = pygame.time.Clock()

background_image = pygame.image.load('background.png')
hero_image = pygame.image.load('hero.png')
goblin_image = pygame.image.load('goblin.png')
monster_image = pygame.image.load('monster.png')
arrow_image = pygame.image.load('Arrow.png')

#background music created via pygame
bg_music = pygame.mixer.Sound('bg.wav')
bg_music.play()

# ======= INTRO SCREEN LOOP =======

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if (event.key == 32):
                    intro = False
                
        pygame_screen.fill(white)
        pygame.display.update()

game_intro()

# ==========MAIN GAME =============
game_on = True
# the loop will run as long qas our bool is true
while game_on:
    # we are in the game loop from here on out
    # 5. Listen for events and quit if the user clicks the x
    # ======= EVENT LISTENER =======
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            # THE USER CLICKED THE RED DOT!
            game_on = False
        elif (event.type == pygame.KEYDOWN):
            # THE USER PRESSED A KEY
            if (event.key == 273):
                #the user pressed the up arrow!!! Move our dude up
                # theHero.y -= 10
                theHero.shouldMove("up")
            elif (event.key == 274):
                #the user pressed the down arrow!!! Move our dude down
                # theHero.y += 10
                theHero.shouldMove("down")
            elif (event.key == 275):
                #the user pressed the right arrow!!! Move our dude right
                # theHero.x = 10
                theHero.shouldMove("right")
            elif (event.key == 276):
                #the user pressed the left arrow!!! Move our dude left
                # theHero.x -= 10
                theHero.shouldMove("left")
            elif (event.key == 32):
                #Space bar..... FIRE!!!!
                new_arrow = Arrow(theHero)
                arrows.add(new_arrow)

                
        elif (event.type == pygame.KEYUP):
            # the user RELEASED a key
            if (event.key == 273):
                theHero.shouldMove("up", False)
            elif (event.key == 274 ): 
                theHero.shouldMove("down", False)
            elif (event.key == 275):
                theHero.shouldMove("right", False)
            elif (event.key == 276):
                theHero.shouldMove("left", False) 

    # ======= DRAW STUFF =======
    # we use blit to draw on the screen. blit = block image transfer
    # blit is a method that takes 2 args:
    # 1. What to draw
    # 2. Where to draw it - Starts at 0,0 
    # top left = 0,0
    # top right = 0,480
    # bottom = 512, 0 
    # bottom right = 512 , 480
    pygame_screen.blit(background_image,[0, 0])

    pygame_screen.blit(hero_image,[theHero.x, theHero.y])
    theHero.drawMe()

    # draw the bad guys
    for badGuy in badGuys:
        badGuy.update_me(theHero)
        pygame_screen.blit(monster_image,[badGuy.x, badGuy.y])

    #draw the arrows
    for arrow in arrows:
        arrow.updateMe()
        pygame_screen.blit(arrow_image, [arrow.x, arrow.y])

        
    # create multiple bad guys

    # if arrow hits badGuys, this will remove both (hence both true)
    arrowHit = groupcollide(arrows, badGuys, True, True)

    # make point counter that increments each time your arrow hits the goblin


    # make collision between badGuy and goodguy
    heroHit = groupcollide(hero, badGuys, True, True)

    
    # If hero is hit via collision, game closes out, need to change this 
    # to create a message
    if heroHit: 
        game_on = False
    # if game is over, give them their point total of bad guys slain, 
    # give them the option to end the game/quit or start over

    pygame.display.flip()
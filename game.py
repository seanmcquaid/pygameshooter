# miniconda access to run pygame
# cd ~/miniconda/bin
# source activate py3k
# cd ~/development/11:18\ -\ Immersive/unit1/pygame_shooter
# python game.py

# 1. include pygame 
import pygame

# 2. initialize pygame
pygame.init()

# 3. make a screen with a size. The size MUST be a tuple
# made screen size equal to background image size
screen_size = (512, 480)
pygame_screen = pygame.display.set_mode(screen_size)
# 4. set the title of the window that opens
pygame.display.set_caption('Robin Hood')

# ==========VARIABLES FOR OUR GAME ===============
background_image = pygame.image.load('background.png')
hero_image = pygame.image.load('hero.png')
goblin_image = pygame.image.load('goblin.png')
monster_image = pygame.image.load('monster.png')
arrow_image = pygame.image.load('Arrow.png')
heroLoc = {
    'x': 0,
    'y': 0 
}

# ==========MAIN GAME LOOP =============
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
            if (event.key == 273 and heroLoc['y'] > 0):
                #the user pressed the up arrow!!! Move our dude up
                heroLoc['y'] -= 15
            elif (event.key == 274 and heroLoc['y'] < 448):
                #the user pressed the down arrow!!! Move our dude down
                heroLoc['y'] += 15
            elif (event.key == 275 and heroLoc['x'] < 480):
                #the user pressed the right arrow!!! Move our dude right
                heroLoc['x'] += 15
            elif (event.key == 276 and heroLoc['x'] > 0):
                #the user pressed the left arrow!!! Move our dude left
                heroLoc['x'] -= 15
            else:
                print (event.key)

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
    pygame_screen.blit(hero_image,[heroLoc['x'], heroLoc['y']])
    pygame.display.flip()
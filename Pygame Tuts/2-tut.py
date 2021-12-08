import pygame
pygame.init()           # Initialize

"""
x = pygame.init()       # It initialize all moduls of pygame
print(x)                # (5, 0) --> 5 initialize, 0 uninitialize
"""

#-----------------------Create Display Window------------------------
gameWindow = pygame.display.set_mode((1200, 500))       #it takes parameter tuple(Width, Height)

#-----------------------Create Title Name/Caption---------------------------
pygame.display.set_caption("My First Game")

"""
Every game has event:
    -> Start game
    -> End game
    -> Game over
These are all work as user input by keyboard/mouse
"""

#--------------------Game specific variables are required-------------------that are handle in game loop
exit_game = False           # If this is True then exit_game
game_over = False           # If this is True then game_over

#---------------------------Creating a game loop----------------------------
""" All events/actions handle by game loop 
    infinite while loop
"""
while not exit_game:            # infinite while loop
    for event in pygame.event.get():
        # print(event)        # print all movement or actions taken by user
        #---------------------For exit game key working------------------
        if event.type == pygame.QUIT:
            exit_game =True

        if event.type == pygame.KEYDOWN:                          # For know what key pressed
            if event.key == pygame.K_RIGHT:                       # For take right arrow key 
                print("You have pressed right arrow key")

pygame.quit()
quit()
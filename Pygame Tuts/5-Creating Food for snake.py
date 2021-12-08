import pygame
import random

pygame.init()

screan_width = 900
screan_height = 600

# Creating window
gameWindow = pygame.display.set_mode((screan_width, screan_height))

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0,0,0)

# Game Title
pygame.display.set_caption("Snake By IRFAN")
pygame.display.update()                             # for change what you

#Game specific variable
exit_game = False
game_over = False
snake_x = 45
snake_y = 55
# velocity_x = 4              #------Moves Diagonaly
# velocity_y = 4              #------Moves Diagonaly
velocity_x = 0              #---Initial it has to zero
velocity_y = 0              #---Initial it has to zero

food_x = random.randint(0, screan_width)                # random number generate
food_y = random.randint(0, screan_height)               # random number generate
snake_size = 10
fps = 30                         # Frame per second

Clock = pygame.time.Clock()                          # We have to update w.r.t. time


# Game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        
        if event.type == pygame.KEYDOWN:
            #----------------For Right(x) Movement----------------
            if event.key == pygame.K_RIGHT:
                # snake_x = snake_x + 10        #---Velocity_x has to change
                velocity_x = 4
                velocity_y = 0

            #----------------For Left(x) Movement-----------------
            if event.key == pygame.K_LEFT:
                # snake_x = snake_x - 10
                velocity_x = -4
                velocity_y = 0

            #----------------For UP(y) Movement-------------------
            if event.key == pygame.K_UP:
                # snake_y = snake_y - 10
                velocity_y = -4
                velocity_x = 0

            #----------------For Down Movement--------------------
            if event.key == pygame.K_DOWN:
                # snake_y = snake_y + 10
                velocity_y = 4
                velocity_x = 0


    snake_x += velocity_x
    snake_y += velocity_y



    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, red,[food_x, food_y, snake_size, snake_size])          # Generating red color ractangle food for snake 
    #--------------------------For creating snakes head(rectangle)------------
    pygame.draw.rect(gameWindow, black,[snake_x, snake_y, snake_size, snake_size])          #(where you want to make, what is color, list of position and size of snake)

    pygame.display.update()         # For update what you want to change
    Clock.tick(fps)


pygame.quit()
quit()
# Imports
import pygame
import math
import random

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "My Awesome Picture"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125 , 0)
YELLOW = (255, 238, 0)
OCEAN = (0, 116, 112)
BROWN = (139, 69, 19)
SKY = (202, 217, 252)
RAIL = (201, 192, 187)
BOAT = (101, 67, 33)


    
''' Make Star '''
stars = []
for i in range(200):
    x = random.randrange(0, 800)
    y = random.randrange(0, 400)
    r = random.randrange(1, 5)
    s = [x, y, r, r]

def draw_cloud(x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])

# Game loop
done = False


while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #Drawing code
    ''' sky '''
    screen.fill(SKY)

    ''' stars '''
    for s in stars:
        pygame.draw.ellipse(screen, YELLOW, S)

    ''' moon '''
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])

    ''' grass '''
    pygame.draw.rect(screen, OCEAN, [0, 390, 850, 210])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        post = [x+5, y], [x+10, y+5], [x+10, y+40], [x, y+40], [x, y+5]
        postt = [x+10,y]
        pygame.draw.polygon(screen, OCEAN, post)

    pygame.draw.rect(screen, OCEAN, [0, y+10, 800, 5])
    pygame.draw.rect(screen, OCEAN, [0, y+10, 800, 5])


    ''' deck '''
    pygame.draw.rect(screen, BROWN, [500, 315, 700, 30])

    ''' pillars '''
    pygame.draw.rect(screen, BROWN, [500, 320, 20, 300])

    ''' railing '''
    pygame.draw.rect(screen, RAIL, [500, 320, 10, 10])

    ''' boatbase '''
    pygame.draw.polygon(screen, BOAT, [[150,325], [200,400], [400,400], [450,325]])

    ''' flag '''
    pygame.draw.rect(screen, BROWN, [270, 225, 20, 100])

    ''' flag '''
    pygame.draw.rect(screen, RED, [270, 200, 70, 40])

    ''' clouds '''
    draw_cloud(100, 50)
    draw_cloud(400, 15)
    draw_cloud(250, 85)
    draw_cloud(500, 90)
    draw_cloud(700, 10)

                                     
    #Update Screen
    pygame.display.flip()
    clock.tick(refresh_rate)



    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()

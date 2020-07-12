"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame

import mido
mid = mido.MidiFile('boxingday.mid', clip=True)
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()



# Set the width and height of the screen [width, height]
size = (1500, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

gitImg = pygame.image.load('guitar.png')
def guitar(x,y):
    screen.blit(gitImg, (x,y))

#x =  (size[0] * 0.45)
#y = (size[1]* 0.8)
x = 0
y = 0
rect_x = 50
# string positions for each string
stringPos = {1: 35, 2: 80 , 3 : 125, 4 : 170, 5: 215, 6 : 260}
fretPos = {1:100, 2: 205, 3 : 305, 4 : 400, 5 : 485, 6 : 570, 7 : 650, 8 : 723, 9 : 790, 10 : 855, \
           11: 920, 12: 978, 13: 1033, 14: 1081 , 15: 1132, 16: 1180, 17: 1225, 18: 1266, 19: 1305,\
           20 : 1343, 21 : 1378, 22 : 1413}
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        pygame.draw.rect(screen, BLACK, [rect_x, 50, 50, 50])
        rect_x += 1

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
    guitar(x, y)

    # --- Drawing code should go here

    pygame.draw.circle(screen, (0, 0, 255), (fretPos[22], stringPos[5]), 12, 0)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
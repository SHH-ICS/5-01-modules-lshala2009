# Using the pygame library, draw a simple picture. 
# It can be anything you like, but you must use at least 2 different types of shapes and 3 different colors.


#I drew a bird if you cant tell 



import pygame

from pygame import Color, Rect
from pygame import draw
from pygame import display

SCREEN_SIZE = (500, 500)

# initialize pygame modules
pygame.init()

# get a surface for graphics display
gameDisplay = display.set_mode(SCREEN_SIZE)

# background - color of the sky
gameDisplay.fill(Color('lightblue'))

# draw a house with a roof
draw.rect(gameDisplay, Color('salmon'), Rect(500, 600, 700, 800))
draw.polygon(gameDisplay, Color('brown'), [(10, 200), (400, 200), (250, 50)])

# draw green grass
draw.rect(gameDisplay, Color('white'), Rect(0, 400, 500, 100))

# draw a sun
draw.circle(gameDisplay, Color('orangered'), (100, 100), 200)

# draw a ball

draw.circle(gameDisplay, Color('black'), (200, 100), 40)

#draw a ball

draw.circle(gameDisplay, Color('white'), (187, 97) ,10)

#

# show the graphics on the screen
display.flip()

# Wait for user input before closing the window
input("Press enter to exit")
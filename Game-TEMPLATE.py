#####################################################################
# author: Connor Heard   
# date: 3 / 17 / 2023   
# description: Program 2 - Person Class Reloaded
#####################################################################
import pygame
from random import randint, choice
from Item import *
from Constants import *


# A person class for the game; Used to signify the player controlled sprite
class Person(pygame.sprite.Sprite, Item):
    def __init__(self):
        # Inherits all the states and behaviors from the Item class
        Item.__init__(self)

        # Creates a square surface in the top left corner of window
        self.surf = pygame.Surface((self.size, self.size))

        # Fills the square with color black initially
        self.color = BLACK
        self.surf.fill(self.color)

   # Mutators and accessors for Person's instance variables     
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):      
        self._color = value

    @property
    def surf(self):
        return self._surf

    @surf.setter
    def surf(self, value):
        self._surf = value

######################### BEHAVIORS ###########################

    # Randomly selects a color from the COLOR list
    # In the Constants library and sets updates the color as such
    def setColor(self):
        self.color = choice(COLORS)

    # Updates the size of the object to a randomly selected size
    # between 10 and 100
    def setSize(self):
        self.size = randint(10, 100)

    # The update function checks to see if the user presses any arrow
    # keys and updates the sprite's position accordingly;
    # When the space bar is pressed, the sprite is changed to a
    # random color and random size and then updated accordingly
    def update(self,pressed_keys):
        if pressed_keys[K_UP]:
            self.goUp()
        if pressed_keys[K_DOWN]:
            self.goDown()
        if pressed_keys[K_LEFT]:
            self.goLeft()
        if pressed_keys[K_RIGHT]:
            self.goRight()
        if pressed_keys[K_SPACE]:
            self.setColor()
            self.setSize()
            self.surf = pygame.Surface((self.size, self.size))
            self.surf.fill(self.color)

    # Sets the sprite's position to a random coordinate
    # within the window
    def setRandomPosition(self):
        random_x = randint(0,WIDTH)
        random_y = randint(0, HEIGHT)
        self.x = random_x
        self.y = random_y

    # Returns the center x & y coordinates of the sprite
    def getPosition(self):
        x_center = self.x - self.size / 2
        y_center = self.y - self.size / 2
        return ((x_center, y_center))

    def __str__(self):
        return "{} color = {}".format(Item.__str__(self), self.color)



########################### main game################################
# DO NOT CHANGE ANYTHING BELOW THIS LINE
#####################################################################

# Initialize pygame library and display
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a person object
p = Person()
clock = pygame.time.Clock()
RUNNING = True  # A variable to determine whether to get out of the
                # infinite game loop

while (RUNNING):
    # Look through all the events that happened in the last frame to see
    # if the user tried to exit.
    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key == K_ESCAPE):
            RUNNING = False
        elif (event.type == QUIT):
            RUNNING = False
        elif (event.type == KEYDOWN and event.key == K_SPACE):
            print(p)

    # Otherwise, collect the list/dictionary of all the keys that were
    # pressed
    pressedKeys = pygame.key.get_pressed()
    
    # and then send that dictionary to the Person object for them to
    # update themselves accordingly.
    p.update(pressedKeys)

    # fill the screen with a color
    screen.fill(WHITE)
    # then transfer the person to the screen
    screen.blit(p.surf, p.getPosition())
    pygame.display.flip()
    clock.tick(110)

pygame.quit()

#####################################################################
# author: Connor Heard      
# date: 3 / 10 / 2023       
# description: Program 1 - Person Class
#####################################################################

from math import sqrt
# global Constants to restrict the maximum x and y values that a person object
# can have.
MAX_X = 800
MAX_Y = 600

# A class representing a person. A person can be initialized with a
# name, as well as x and y coordinates. However, there are default
# values for all those (i.e. player 1, 0 and 0 respectively). A person
# also has a size which is set to 1 by default. A person can go left, 
# go right, go up and go down. A person also has a string function 
# that prints out their name location, and size. A person also has a 
# function that calculates the euclidean distance from another person 
# object.
class Person:
    # Function initializes the Person class. Sets the default name, x, and y  to "player 1", 0, and 0, respectively.
    def __init__(self, name = "player 1", x = 0, y = 0):
        self.name = name
        self.x = x
        self.y = y
        self.size = 1

    # Accessor and mutator for the name state; if the len of the string inputted by the user is less than 2, then the name is set to
    # the default value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, input):
        if (len(input) < 2):
            self._name = "player 1"
        else:
            self._name = input

    # Accessor and mutator of the x state; checks to make sure that the user arguements are between 0 and the Max x-value.
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, input):
        if (input < 0):
            self._x = 0
        elif (input > MAX_X):
            self._x = MAX_X
        else:
            self._x = input

    # Accessor and mutator of the y state; checks to make sure that the user arguements are between 0 and the Max y-value.
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, input):
        if (input < 0):
            self._y = 0
        elif (input > MAX_Y):
            self._y = MAX_Y
        else:
            self._y = input

    # Accessor and mutator of the size state; checks to make sure that the user arguement is large than or equal to 1.
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, input):
        if (input >= 1):
            self._size = input

    ###################### Behaviors #################################

    # moves the player to the left according to the input
    def goLeft(self, distance = 1):
        self.x -= distance

    # moves the player to the right according to the input
    def goRight(self, distance = 1):
        self.x += distance

    # moves the player up according to the input
    def goUp(self, distance = 1):
        self.y -= distance

    # moves the player down according to the input
    def goDown(self, distance = 1):
        self.y += distance

    # calculates the distance between two Person objects
    def getDistance(self, other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    # returns a string that gives the current state of the object
    def __str__(self):
        return ("Person({}):\tsize = {},\tx = {}\ty = {}".format(self.name, self.size, self.x, self.y))
    

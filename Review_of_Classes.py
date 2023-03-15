# Inheritance
# - child classes inherit the state/behavior of
# the parent class
# - state: what is the class? (instance variables)
# - behavior: what can the class do? (functions)
# "child" is a "parent" relationship
# instance variables

# First box tells you the class name
# - word after colon is the data type
# Second box in diagram tells you the instance variables
# Third box tells you the behaviors/functions

class Vehicle:
    def __init__(self, name):
        self.tires = None
        self.engine = None
        self.name = name

    def __str__(self):
        return "owner={}, tires={}, engine={}".format(self.name, self.tires, self.engine)

class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)
        self.tires = 4
        self.engine = True

    def __str__(self):
        return "Car; " + super().__str__()

class Cycle(Vehicle):
    def __init__(self, name):
        super().__init__(name)
        self.tires = 2
        
    def __str__(self):
        return super().__str__()

class Bicycle(Cycle):
    def __init__(self, name):
        super().__init__(name)
        self.engine = False

    def __str__(self):
        return "Bicycle; " + super().__str__()

class Motorcycle(Cycle):
    def __init__(self, name):
        super().__init__(name)
        self.engine = True

    def __str__(self):
        return "Motorcycle; " + super().__str__()




c1 = Car("Connor")
b1 = Bicycle("Bob")
m1 = Motorcycle("Johnny")
print(c1)
print(b1)
print(m1)

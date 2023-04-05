#####################################################################
# author: Connor Heard      
# date: 3 / 29 / 2023        
# description: Program 3: Employee Class 
#####################################################################

# import the abc library to make abstract classes
import abc

######################################################################
# An employee class. Its constructor takes the first name, last name and
# pay. It also has email and position as instance variables. It contains
# a single abstract method i.e. applyRaise, and a createEmail function
# that creates an appropriate email address from the employee's first
# and last names.
######################################################################
class Employee(metaclass = abc.ABCMeta):
    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = self.createEmail()
        self.position = None

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, value):
        value = value.strip()
        value = value.capitalize()
        self._firstname = value

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, value):
        value = value.strip()
        value = value.capitalize()
        self._lastname = value
        

    @property
    def pay(self):
        return self._pay

    @pay.setter
    def pay(self, value):
        if (value >= 20000):
            self._pay = value
        else:
            self._pay = 20000

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if ("@latech.edu" in value):
            self._email = value
        else:
            self._email = self.createEmail()

####################### Behaviors ###############################

    def createEmail(self):
        return ((self.firstname + "." + self.lastname + "@latech.edu").lower())

    @abc.abstractmethod
    def applyRaise(self, rate):
        raise NotImplementedError("Abstract method applyRaise not implemented in subclass!")

    def __str__(self):
        return (self.lastname + ", " + self.firstname + " (" + self.email + ")")


######################################################################
# A faculty class is a subclass of the Employee class above. Its
# constructor receives both names as well as the position. The Faculty
# class also overrides the applyRaise function by multiplying the pay by
# the rate provided as an argument. It also slightly tweaks the __str__
# function in the super class.
######################################################################
class Faculty(Employee):
    def __init__(self, firstname, lastname, position):
        self.pay = 50000
        Employee.__init__(self, firstname, lastname, self.pay)
        self.position = position

    def applyRaise(self, rate):
        if (rate > 0):
            self.pay = rate * self.pay
        else:
            pass

    def __str__(self):
        return (super().__str__() + " -- " + self.position)
            

######################################################################
# A Staff class is a subclass of the Employee class above. Its
# constructor only receives both names. It also overrides the applyraise
# function but adding the increase (provided as the argument) to the
# pay. It doesn't change anything else from the Employee class.
######################################################################
class Staff(Employee):
    def __init__(self, firstname, lastname):
        self.pay = 40000
        Employee.__init__(self, firstname, lastname, self.pay)

    def applyRaise(self, rate):
        if (rate > 0):
            self.pay = rate + self.pay
        else:
            pass

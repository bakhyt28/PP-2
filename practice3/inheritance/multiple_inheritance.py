class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

class Graduation:
    def __init__(self, year):
        self.graduationyear = year

# Multiple inheritance
class Student(Person, Graduation):
    def __init__(self, fname, lname, year):
        Person.__init__(self, fname, lname)
        Graduation.__init__(self, year)

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# Testing
x = Student("Mike", "Olsen", 2019)
x.welcome()
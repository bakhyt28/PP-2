# Parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Child class inherits from Person
class Student(Person):
    pass  # no additional properties yet

# Testing
x = Student("Mike", "Olsen")
x.printname()  # inherited method from Person
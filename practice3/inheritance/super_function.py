# Parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

# Child class using super() to inherit parent's __init__
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)  # inherit properties
        self.graduationyear = year      # new property

# Testing
x = Student("Mike", "Olsen", 2019)
print(x.firstname, x.lastname, x.graduationyear)
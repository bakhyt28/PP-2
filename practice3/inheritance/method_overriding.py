class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def greet(self):
        print("Hello,", self.firstname, self.lastname)

# Child class overrides greet method
class Student(Person):
    def greet(self):  # override method
        print("Welcome", self.firstname, self.lastname, "to the class!")

# Testing
x = Student("Mike", "Olsen")
x.greet()  # uses overridden method
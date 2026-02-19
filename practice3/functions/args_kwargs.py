#1
def my_function(*kids):  # *kids allows passing any number of arguments (stored as a tuple)
  print("The youngest child is " + kids[2])  # access the third element (index starts from 0)

my_function("Emil", "Tobias", "Linus")  # passing three arguments

#2
def my_function(username, **details):  # username is required, **details stores extra named arguments as a dictionary
  print("Username:", username)  # print the main argument
  print("Additional details:")
  for key, value in details.items():  # loop through dictionary (key-value pairs)
    print(" ", key + ":", value)

my_function("emil123", age=25, city="Oslo", hobby="coding")  # passing keyword arguments

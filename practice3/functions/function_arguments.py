def my_function(country="Norway"):  # default parameter
  print("I am from", country)

my_function("Sweden")  # override default value
my_function("India")
my_function()  # uses default value
my_function("Brazil")
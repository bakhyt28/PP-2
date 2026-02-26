#1
def square_generator(limit):
    # generate squares of numbers from 1 to limit
    for num in range(1, limit + 1):
        yield num * num   # return square of the number


user_number = int(input())   # read number from user

# print all generated squares
for value in square_generator(user_number):
    print(value)



#2
def even_generator(limit):
    # generate even numbers from 0 to limit
    for num in range(0, limit + 1, 2):
        yield str(num)   # convert number to string for printing


user_limit = int(input())   # read input number

is_first = True   # flag to avoid comma before first element

# print numbers separated by commas
for value in even_generator(user_limit):
    if not is_first:
        print(",", end="")   # print comma before next number
    print(value, end="")     # print number in one line
    is_first = False



#3
def divisible_by_three_and_four(limit):
    # generate numbers divisible by both 3 and 4
    for num in range(0, limit + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num   # return number if condition is true


input_number = int(input())   # read number from user

first_element = True   # flag to control comma placement

# print numbers separated by commas
for value in divisible_by_three_and_four(input_number):
    if not first_element:
        print(",", end="")   # print comma between numbers
    print(value, end="")     # print number
    first_element = False
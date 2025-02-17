#------------------------Beginner-Level----------------------------#
from audioop import reverse

from Tools.demo.sortvisu import demosort

# 1. Write a program to find the length of the string 'Hello World!' using a built-in function.
hallo_world = "Hallo World"
print(len(hallo_world))

# 2. Use the type() function to check the data type of the variable my_var = 3.14.
my_var = 3.14
print(type(my_var))

# 3. Calculate the sum of all numbers in the list [5, 10, 15] using a built-in function.
calculate_sum = [5,10,15]
print(sum(calculate_sum))


# 4. Use the min() function to find the smallest number in [8, 3, 12, 7].

smallest_num = [8,3,12,7]
print(min(smallest_num))

# 5. Write a program that takes user input and prints it in uppercase using a built-in function.
user_name = input("Please enter your name :\n").upper()
print(user_name)


#------------------Intermediate-Level-----------------------------#
# 1. Sort the list [10, 5, 8, 3] in ascending and descending order using a built-in function.
list_num = [10,5, 8,3]
list_num.reverse()
print(list_num)
print(sorted(list_num))
# 2. Write a program that accepts a list of numbers and filters out the odd numbers using the
# filter() function.
# 3. Use the zip() function to merge two lists: ['John', 'Jane'] and [80, 90].

name_1= ["John","Jane"]
marks = [80,90]
name_marks = zip(name_1, marks)
print(list(name_marks))
# 4. Write a program that rounds a floating-point number (e.g., 3.7654) to 2 decimal places
round_float_num = 3.7654
print(round(round_float_num))
# using a built-in function.
# 5. Write a program that maps a function to square each number in the list [2, 4, 6, 8].
map_square = [2,4,6,8]
print(map_square)
# Advanced-Level
# 1. Write a program to evaluate a mathematical expression entered by the user using eval().
# 2. Create a program that combines two lists (e.g., names and marks) into a dictionary using
# the zip() function.
# 3. Write a program that generates the Fibonacci sequence up to 10 terms using range() and
# list().
# 4. Use the map() function to apply a function that capitalizes each string in ['python', 'java',
# 'c++'].
# 5. Write a program to filter out words shorter than 4 letters from the list ['cat', 'dog',
# 'elephant', 'tiger'] using filter().

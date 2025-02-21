#----------------------------beginner--------------------------------#
#try except function-------------------------------------------------#

'''
 1. Write a function divide_numbers(a, b) that returns the result of a / b. Handle the
 case where b is zero by returning "Cannot divide by zero".
'''

def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "You cannot divide by zero"


result_output = divide_numbers(21,0)
print(result_output)
'''
 2. Write a program that reads an integer input from the user. Use a try-except block
 to handle Value Error if the user enters invalid data (e.g., a string like "abc").
'''
num1 = input("please enter first number : ")
op = input("")
num2 = input("Please enter second number : ")

try:
    if op == "+":
        resul = int(num1) + int(num2)
        print(resul)
    elif op == "-":
        resul = int(num1) - int(num2)
        print(resul)

    elif op == "/":
        resul = int(num1) / int(num2)
        print(resul)

    elif op == "*":
        resul = int(num1) * int(num2)
        print(resul)
    else:
        print("is not a number")
except ValueError:
    print("Please don't ruin my program enter a number")


'''
 3. Write a small program that prompts the user for their age (as an integer) and uses
 a try-except block to handle ValueError in case the user inputs a non-integer (e.g.,
 "twenty").
'''
try:
    age = int(input("Please enter your Age : \n"))
    print(f"I'm {age} years old \n")
except ValueError:
    print("Please enter numbers")
'''
 4. Create a function convert_to_int_list(str_list) that takes a list of strings (e.g., ["1",
 "2", "abc", "4"]) and returns a new list of integers. Use a try-except block inside a
 loop to handle any ValueError when a string can’t be converted, and print an
 error message without stopping the entire process.
'''
def convert_to_int_list(str_list):
    int_list = []
    for string in str_list:
        try:
            int_list.append(int(string))
        except ValueError:
            print(f"Skipping non integers {string}")
            return int_list


str_list = ['1','2','3','4','rrr']
list_int = convert_to_int_list(str_list)
print(list_int)
'''
 5. Create a function access_list_item(my_list, index) that attempts to return the
 element at index. Handle IndexError by printing a message like "Index out of
 range" if the requested index is invalid.
'''
def access_list_item(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        print("Index out of range")
        return None

list_index = [1,2,3,4,5,6]
print(access_list_item(list_index,3))
print(access_list_item(list_index,10))

'''
 Intermediate
 6. Write a function get_key_value(dictionary, key) that returns the value of a given
 key from a dictionary. Use KeyError handling to print a friendly message if the
 key does not exist.
'''
def get_key_value(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        print("Key does not exist")
        return None

dick_keys = {"Name": "Admire","City": "Tsholotsho","Age" : 38}
print(get_key_value(dick_keys, "Car"))

'''
 7. Create a function calculate_bmi(weight, height) that raises a custom exception
 InvalidHeightError if height is 0 or negative.
'''
def calculate_bmi(weight, height):
    if height <= 0:
        raise InvalidHeightError("Height must be positive")
    return weight / height ** 2

try:
    weight = 22 #kgs
    height = 2 #meters
    bmi_weight_height = calculate_bmi(weight,height)
    print(f"BMI : {bmi_weight_height: .2f}")
except InvalidHeightError as e:
    print(e)

'''
 8. Use the raise keyword to force a TypeError if a function add_numbers(a, b) is
 called with non-integer arguments.
'''
def add_numbers(a, b):
    if not  isinstance(a, int) or not isinstance(b,int):
        raise TypeError("Arguments must be integers")
    return a + b

try:

    print(add_numbers(7,8))
except TypeError as e:
    print(e)

try:
 print(add_numbers(7,"8"))
except TypeError as e:
    print(e)



'''
 9. Create a function safe_division(a, b) that returns the result of a / b. Handle
 ZeroDivisionError with a custom message. Use the else clause to print "Division
successful!" when no exception occurs. Return the result only if successful;
 otherwise, return None
'''
def safe_division(a, b):

    try:
       result3 = a / b
       print("Division successful")
       return result3
    except ZeroDivisionError:
        print("You cannot divide by zero")
        return None

print(safe_division(20,5))
print(safe_division(15,0))
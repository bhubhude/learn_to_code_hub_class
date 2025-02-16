'''
Write a python program to check if a number is positive ,negative or zero
Hint use an if-elif- else statement to compare the number with 0
Expected output  Example
for number = -5 the output should be the number is negative
'''
from numpy.ma.core import count
from unicodedata import digit

number = int(input('Please enter you number: '))

if number == 0:
    print('The number is  zero')

elif number > 0:
    print('The number is positive')

elif number < 0:
    print('The number is  negative')

else:
    print('Is not a number')

# --------------------------------------------------------------------------#

'''
Create a python program that  takes a person age as an input and categorize them
Child 0-12
Teenager 13-19 year
Adult 20-59
Senior 60 + years
'''

age = int(input('Please enter Age : \n'))
if age == 0 or age <= 12:
     print('You are a child')

elif age == 13 or age <= 19:
    print('You are Teenager')

elif age == 20 or age <= 59:
    print('You are Adult')

elif age >= 60:

    print('You are Senior')
else:
    print('Dead person')
#---------------------------------------------------------------------------#

# Create a program that uses nested loops to print the following
'''1
123
1234
12345'''

for i in range(1,6):
    for j in range(1,i + 1):
        print(j,end="")
    print()

#----------------------------------------------------------------------------------------------#

'''Write a Python program that calculates the grade of a student based on their score using these
conditions:'''
# 90 and above: Grade A
# 80–89: Grade B
# 70–79: Grade C
# 60–69: Grade D
# Below 60: Grade F
# Expected Output Example:
# For score = 85, the output should be: Your grade

def calculated_grade(score):
    if score >= 90:
        return "Your grade is A"


    elif score >= 80:
        return "Your grade is B"

    elif score >= 70:
        return "Your grade is C"

    elif score >= 60:
        return "Your grade is D"

    elif score < 60:
        return "Your grade is F"

    else:
        return "You entered wrong value"

score = float(input("Enter Score Number :\n"))
print(calculated_grade(score))
#------------------------------------------------------------------------------------------#
# Write a program to print all the numbers from 1 to 10 using a for loop
for numbers in range(0, 10):
    numbers += 1
    print(numbers)

#---------------------------------------------------------------------#
# Write a program that asks the user to input a number and then counts down to 0 using a while
# loop. Output Example:
# Input: 5
# Output: "5, 4, 3, 2, 1, 0"
def countdown(n):
    count = n
    result = " "
    while count >= 0:
        result += str(count)
        if count > 0:
            result += ", "
        count -=1
    return result


nums = int(input('Enter your number : \n'))
print(countdown(nums))

#Create a Python program that calculates the sum of all even numbers between 1 and 50 using a
#for loop. Hint: Use the range() function with
#steps of 2 to iterate over even numbers. Expected Output Example:
#("The sum of even numbers from 1-50 is 650")
def sum_even_numbers(start, end):
    even_sum = 0
    for num in range(start, end + 1,2):
        even_sum += num
    return even_sum
#-----------------------------------------------------------------------------#

start = 1
end = 50
result = sum_even_numbers(start, end)
print(f'The sum of even number {start} to {end} is {result}:\n\n')

#-----------------------------------------------------------------------#
#even number with python

even_number = []
for i in range(1,51):
    if i % 2 == 0:
        even_number.append(i)
print(even_number)

# Write a Python program that simulates a simple guessing game:
# 1. Use a while loop to ask the user to guess a number between 1 and 20.
# 2. If the guess is correct, print “Congratulations! You guessed it!” and exit the loop.
# 3. If the guess is too high or too low, provide feedback and let them guess again.
# 4. The program should stop after 5 incorrect attempts and print “Game Over.”
# Hint:
#  Use a random number generator (random.randint()) to set the correct number.
#  Use a counter to track the number of attempts.

import random
def guessing_game():
    correct_number = random.randint(1,20)
    attempts = 0
    max_attempts = 5
    print("Welcome to the Guessing game")
    print("Pick a number from 1 and 20")

    while attempts < max_attempts:
        guess = int(input("Take a Guess \n"))
        attempts += 1

        if guess == correct_number:
            print(f"Congratulations you have guessed number in {attempts} attempts \n")
            return

        elif guess < correct_number:
            print("The number is too low Try again\n")

        else:
            print("The number is to high \n")

        # User  exceeds the number of attempts
    print(f"Game over! The correct number was {correct_number} \n")

guessing_game()

#Password Checker (If Statement + While Loop)
# Create a program that:
#   Asks the user to enter a password.
#   Checks if the password matches a predefined value (e.g., "python123").
#   If incorrect, lets the user try again.
#   Stop sand prints "Access Granted" when the correct password is entered

def password_checker():
    correct_password = "Python"
    while True:
        user_password = input("please enter your password : \n")
        if user_password == correct_password:
            print("The password is correct")
            break
        else:
            print("password is incorrect try again")


password_checker()

#-----------------------------------------------------------------------------------#
# Write a program that prints a pattern using nested loops:
#  *
#  **
#  ***
#  ****
#  *****
def print_pattern(rows):
    for i in range(rows):
        for j in range(rows - i - 1):
            print("", end = "")
        for k in range(i + 1):
            print("*", end= "")
        print()

num_rows = 5
print_pattern(num_rows)

#-------------------------------------------------------------------------------#
# Create a program that uses nested loops to print the following triangle:
#  1
#  1 2
#  1 2 3
#  1 2 34
#  1 2 345
for i in range(1,6):
    for j in range(1, 1 + i):
        print(j, end="")
    print()

#---------------------Advance Questions---------------------------------#
 # Enhance the grade checker program to handle invalid scores:
 # If the score is less than 0 or greater than 100, print "Invalid score."
 # Hint: Use nested conditional statements or logical operators.

def grade_checker(scores):
    if 0 <= scores <= 100:

        if scores >= 90:
            print("Grade : A")
        elif scores >= 80:
            print("Grade : B")
        elif scores >= 70:
            print("Grade : C")
        elif scores >= 60:
            print("Grade : D")
        elif scores < 60:
            print("Grade : Fail")
        else:
            print("Invalid Grade")


grade_checker(95)
grade_checker(84)
grade_checker(78)
grade_checker(62)
grade_checker(38)
grade_checker(110)


#------------------------------------------------------------------------------------------------#
'''
Guessing Game with Enhanced Feedback
Improve the guessing game to:
Include a scoring system where closer guesses receive fewer penalty points.
Display the final score when the game ends.
'''

import random

def guessing_game():
    secret_number = random.randint(1, 100)
    attempts_left = 7
    scores = 100

    print("Welcome to the Guessing Game !!")
    print("I have chosen  a number between 1 and 100 .Try To Guess it")

    while attempts_left > 0:
        print(f"\nYou have {attempts_left} attempts remaining")

        try:
            guess = int(input("Please enter your Guessing number :\n"))
        except ValueError:
            print("Invalid input Please enter a number")
            continue

        if guess == secret_number:
            print(f"Congratulations! you have guessed the number in {7 - attempts_left + 1} attempts")
            print(f"Your final Score is {scores}")
            return


        defference = abs(guess - secret_number)
        penalty = 0
        if defference <= 5:
            penalty = 1

        elif defference <= 10:
            penalty = 3

        elif defference <= 20:
            penalty = 5

        else:
            penalty = 7

        scores -= penalty

        if guess > secret_number:
            print(f"Too high ! Score penalty : {penalty}")

        else:
            print(f"Too low ! Score penalty : {penalty}")

        attempts_left -= 1
    print(f"Game over ! The number was {secret_number}.")
    print(f"Your final score is {scores}.")


guessing_game()

# Write a Python program to calculate the sum of the digits of a given number:
 #Input Example: 1234
 #Output Example: "The sum of digits is 10."
def sum_of_digits(n):
     return "The sum of digits is " + str(sum(int(digit) for digit in str(n)))

num = int(input("Please enter number: \n"))
print(sum_of_digits(num))

# Write a program that finds and prints all prime numbers between 1 and 100.
 #Hint: Use nested loops to check divisibility for each number

def is_prime_num(n):
     for num in range(2, n + 1):
         is_prime = True

         for divisor in range(2, int(num ** 0.5) + 1):
             if num % divisor == 0:
                 is_prime = False
                 break

         if is_prime:
             print(num)


is_prime_num(100)
#---------------------------------------------------#
# Modify the countdown timer program to include:
# Adelay of 1 second between each number (use time.sleep(1)).
#Acustom message at the end, like "Time's up!"

import time
def count_down_timer(seconds, custom_message="Time up !!"):
    for time_sec in range(seconds, 0, -1):
        print(time_sec)
        time.sleep(1)
    print(custom_message)


count_down_timer(10)





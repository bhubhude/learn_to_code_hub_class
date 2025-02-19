#-----------------------Beginner Assignment-----------------------------#
#function assignment
'''
 Write a function greet(name) that takes a person's name as input and prints a
 personalized greeting:
 "Hello, <name>! Welcome to the world of Python!".
 Test the function by calling it with your name.
'''

def  greet(name, surname):
    print(f"Hello {name} {surname} Welcome to the world of Python!")


greet("Admire", "Ncube")

'''
Create a function make_pancake(flour, eggs, milk) that takes in the amount of flour,
eggs, and milk, and returns the total number of pancakes you can make (based on the formula: 1 cup flour, 1 egg, 1 cup milk makes 4 pancakes). Call the function and print
the result.
'''


def make_pancake(flour,egg, milk):
    flour_batches = flour  // 1
    egg_batches = egg // 1
    milk_batches = milk // 1
    batches = min(flour_batches, egg_batches,milk_batches)
    total_pancake = batches * 4
    return total_pancake

flour = 3
egg = 4
milk = 3
total_pancake = make_pancake(flour,egg, milk)
print(f"With {flour} of flour , {milk} of milk and {egg} of eggs you can make {total_pancake} of pancakes ")


'''
Temperature Converter:
Write a function convert_to_fahrenheit(celsius) that converts a temperature from
Celsius to Fahrenheit.
Formula: (Celsius * 9/5) + 32 = Fahrenheit. Call the function with a temperature of
20°C.
'''

def convert_to_fahrenheit(celsius):
    return (celsius * 9/5 ) + 32


temperature_fahrenheit = convert_to_fahrenheit(2)
print(f"{20} C is equal to {temperature_fahrenheit} F")

'''
4. NumberCruncher:
 Create a function add_two_numbers(num1, num2) that takes two numbers as
 arguments and returns their sum. Test the function by adding 3 and 7.
'''
def add_two_numbers(num1, num2):
    return num1 + num2

add_nums = add_two_numbers(3, 7)
print(f"Sum of 3 and 7 is : {add_nums}")

'''
5. ThePersonalized Welcome:
 Write a function personalized_welcome(name) that takes a name and prints out:
 "Welcome, <name>! You are doing amazing!". Try calling the function with different
 names.
'''

def personalized_welcome(name, surname):
    print(f"Welcome, {name} {surname}! You are doing amazing! ")


personalized_welcome("Admire", "Ncube")
personalized_welcome("Amahle", "Ncube")
personalized_welcome("Tebogo", "Dube")
personalized_welcome("Aqhamile","Nyathi")
personalized_welcome("Innocentia", "Nkomo")

#-----------------------------Intermediate Level-------------------------------#
'''
 Write a function math_quiz(num1, num2) that accepts two numbers and returns the
 sum, difference, product, and quotient of these two numbers in a tuple. For example:
 (sum, difference, product, quotient). Call the function with 5 and 3.
'''
def math_quiz(num1, num2):
    if num2 == 0:
         return "Error Division by zero is not allowed"

    sum_result = num1 + num2
    diff_result = num1 - num2
    prod_result = num1 * num2
    quot_result = num1 / num2
    return sum_result, diff_result ,prod_result ,quot_result

num1 = 12
num2  = 3
results = math_quiz(num1, num2)
print(f"Sum : {results[0]}")
print(f"Difference : {results[1]}")
print(f"Product : {results[2]}")
print(f"Quotient : {results[3]}")

'''        
 2. Magic Box:
 Create a function magic_box(item1, item2) that returns a sentence like: "You have
 placed <item1> and <item2> in the magic box!". Make the items "a book" and "a
 pen". Test the function with different items.
'''
def magic_box(item1, item2):
    #two items inside the magic box must be strings(str)
    sentence = f"You have placed {item1} and {item2} in the magic box"
    return sentence


print(magic_box(" 8 books"," 12 pens"))
print(magic_box("wallet","pencils"))
print(magic_box("Watches","ear-rings"))
print(magic_box("Spoons","folks"))
print(magic_box("Cabbage"," Carrots"))

'''
 3. Superhero Power Check:
 Write a function can_fly(power_level) that takes the power level of a superhero as
 input and returns "You can fly!" if the power level is greater than 100, or "Try again,
 keep training!" if the power level is 100 or less.
'''
def can_fly(power_level):
    if power_level > 100:
        return "You can fly"
    else:
        return "Try again,keep training!"

print(can_fly(40))
print(can_fly(100))
print(can_fly(120))


'''
4. Shape Area Calculator:
 Create a function calculate_area(shape, dimension1, dimension2=0) that calculates the
 area of a rectangle (length × width) or square (side × side). The second dimension
 should default to 0 for squares. Test your function with both shapes.
'''
def calculated_area(shape,dimension1, dimension2=0):
    if shape.lower() == 'rectangle':
        if dimension2 == 0:
            raise ValueError("With is required for  rectangle")
        return dimension1 * dimension2

    elif shape.lower() == 'square':
        return dimension1 ** 2

    else:
        raise ValueError("You entered invalid shape")


print(calculated_area("rectangle",7,2))
print(calculated_area("Square",7))

'''
5. Discount Finder:
Write a function calculate_discount(price, discount_percentage) that takes the price of
an item and a discount percentage and returns the price after discount. For example, a
price of 100 with a discount of 20% should return 80.
'''
def calculated_discount(price,discount_percentage):
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("The discount percentage must between 0 and 100")
    return price - int((price * discount_percentage / 100))


print(calculated_discount(100,20))


#--------------------------------Advanced Level-----------------------------#
'''
 1. Palindrome Checker:
 Write a function is_palindrome(word) that takes a string and checks if it is a
 palindrome. If it is, return "It’s a palindrome!"; otherwise, return "Not a palindrome!".
 Try it with words like "level" and "hello".
'''
def is_palindrome(word):
    word_palindrome = word.lower()
    reserved_word = word_palindrome[::-1]
    if word_palindrome == reserved_word:
        return "It' s a palindrome word !!"
    else:
        return "It' s not a palindrome word !!"

print(is_palindrome("Hello"))
print(is_palindrome("Madam"))
print(is_palindrome("Refer"))
print(is_palindrome("Civic"))
print(is_palindrome("Animal"))

''' 
 2. Mystery Calculator:
 Create a function mystery_calculation(a, b, c) that accepts three numbers and returns
 the result of the following formula:
 ((a + b) * c) / 2. Call the function with 5, 7, and 10.
'''
def mystery_calculation(a,b,c):
    return ((a + b) * c) / 2

print(mystery_calculation(5,7,10))
'''
 3. Fibonacci Sequence Generator:
 Write a function generate_fibonacci(n) that returns the first n numbers of the
 Fibonacci sequence. For example, for n = 5, the output should be [0, 1, 1, 2, 3].
'''
def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        sequence = [0,1]
        while len(sequence) < n:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence


print(generate_fibonacci(5))



'''
 4. Word Frequency Counter:
 Create a function count_word_frequency(text, word) that takes a string and a word,
 then counts how many times the word appears in the string. Call it with the sentence
 "Python is fun, Python is powerful" and the word "Python".
'''

def count_word_frequency(text, word):
    words = text.split()
    count = sum(1 for w in words if w == word)
    return count

text = "Python is fun, Python is powerful"
word = "Python"
frequency = count_word_frequency(text, word)
print(f"The word {word} appears {frequency} times in the text")

'''
 5. Mystery Number Finder:
 Write a function find_mystery_number(numbers) that accepts a list of numbers and
 returns the largest even number in the list. If there are no even numbers, return "No
 even numbers found!". Test the function with the list [3, 5, 7, 8, 12, 14].
'''
def find_mystery_number(numbers):
    even_nums = [num for num in numbers if num % 2 == 0]
    if not even_nums:
        return "No even numbers found"
    return max(even_nums)

list_numbers = [3, 5, 7, 8, 12, 14]
largest_even_num = find_mystery_number(list_numbers)
print(f"Largest even number in the list is {largest_even_num}")




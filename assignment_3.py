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
print(f"{20} is equal to {temperature_fahrenheit}")


'''
4. NumberCruncher:
 Create a function add_two_numbers(num1, num2) that takes two numbers as
 arguments and returns their sum. Test the function by adding 3 and 7.
 5. ThePersonalized Welcome:
 Write a function personalized_welcome(name) that takes a name and prints out:
 "Welcome, <name>! You are doing amazing!". Try calling the function with different
 names.
 Intermediate Leve

'''
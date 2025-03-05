
#-------------------------------------Project--Practise------------------#
'''
1. Student Management System
 Objective:
 Create a system that helps manage student records by adding, updating, and deleting
 student information.
 Requirements:
1. Allow users to add new students (name, age, grade, student ID).
2. Enable updating a student’s details.
3. Provide an option to delete a student record.
4. Display the list of all students.
5. Implement exception handling to prevent errors (e.g., invalid inputs).
 HowIt Works:
 The program runs a menu system where users choose options like Add Student,
 Update Student, Delete Student, or View All Students.
 Students are stored as objects with attributes like name, age, and grade.
 User scan input a student’s ID to modify or remove them from the system.
'''
from datetime import datetime

class Student:
    def __init__(self,student_id, name, surname,age,grade):
        self.student_id = student_id
        self.name = name
        self.surname =surname
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"ID: {self.student_id} Name: {self.name} Surname: {self.surname} Age: {self.age} Grade: {self.grade}"

class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self):
        try:
            student_id = input("Enter Student ID\t")
            if student_id in self.students:
                print("Student Id already exist in a database")
                return

            name = input("Enter your Name:\t")
            surname = input("Enter your Surname:\t")
            age = int(input("Enter your Age:\t"))
            grade = input("Enter your Grade:\t")
            student = Student(student_id, name, surname, age, grade)
            self.students[student_id] = student
            print("Student Added to the Database Successfully")
        except ValueError:
            print("Age input must be an integer")
        except Exception as e:
            print(f"An error occurred {e}")

    def update_student(self):
        student_id = input("Enter Student ID to update Database")
        if student_id in self.students:
            student = self.students[student_id]
            try:
                name = input(f"Enter new Name {student.name}")
                surname = input(f"Enter new Surname {student.surname}")
                age = int(input(f"Enter new Age: {student.age}"))
                grade = input(f"Enter new Grade {student.grade}")
                if name:
                    student.name = name
                if surname:
                    student.surname = surname
                if age:
                    student.age = int(age)
                if grade:
                    student.grade = grade

                print("Student is successfully updated to the Database")
            except ValueError:
                print("Invalid input age must be an integer")
            except Exception as e:
                print(f"An error occurred {e}")
            else:
                print("Student not found in the Database")

    def delete_student(self):
        student_id = input("Enter Student ID to delete")
        if student_id in self.students:
            del self.students[student_id]
            print("Student successfully deleted in the database")
        else:
            print("Student not found in the database")

    def view_all_student(self):
        if not self.students:
            print("No Student found in the database ")
        else:
            for student in self.students:
                print(student)

    def run_system(self):
        while True:
            print("\nStudent Management System")
            print("1 Add Student")
            print("2 Update Student")
            print("3 Delete Student")
            print("4 View all Student")
            print("5 exit")
            choice = input("Enter your Choice \t")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.update_student()
            elif choice == "3":
                self.delete_student()
            elif choice == "4":
                self.view_all_student()
            elif choice == "5":
                print("Existing Student Management System")
                break
            else:
                print("Invalid choice please try again")

if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.run_system()

'''
 2. Library Catalog System
 Objective:
 Develop a digital library system that tracks available books and manages borrowing
 and returning.
 Requirements:
  User scan add books to the catalog (title, author).
  Allow users to borrow books, changing their status to unavailable.
  Enable users to return borrowed books.
  Display all available books in the catalog.
  Prevent borrowing of already borrowed books using exception handling.
 HowIt Works:
  Books are stored as objects with attributes like title, author, and availability status.
  A user can borrow a book by entering its title. If available, it gets marked as
 borrowed.
  When a book is returned, its status changes back to available.
 '''

class Book:
    def __init__(self ,title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed"if self.is_borrowed else "Available"
        return f"Title: {self.title} Author: {self.author} Status {status}"

class Library:
    def __init__(self):
        self.books = []

    def add_books(self):
        title = input("Enter book Title: ")
        author = input("Enter Author: ")
        book = Book(title,author)
        self.books.append(book)
        print("Book Added Successfully")

    def borrow_book(self):
        title = input("Enter Title of the book to borrow: ")
        for book in self.books:
            if book.title == title:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f"You have borrowed '{book.title}'")
                else:
                    print("The book is already borrowed ")
                return
            print("Book not found")

    def return_book(self):
        title = input("Enter the title of a book to return: ")
        for book in self.books:
            if book.title == title:
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f"You have returned '{book.title}'")
                else:
                    print("Book was not borrowed")
                return
            print("Book not found")

    def display_available_books(self):
        available_books = [book for book in self.books if not book.is_borrowed]
        if not available_books:
            print("No books available")
        else:
            print("Books available")
            for book in available_books:
                print(book)

    def run_library(self):
        while True:
            print("\nDigital Library System")
            print("1. Add Book")
            print("2. Borrow Book")
            print("3. Return Book")
            print("4. View All available Books")
            print("5. Exit")

            choice = input("Please enter your choice: ")
            if choice == "1":
                self.add_books()
            elif choice == "2":
                self.borrow_book()
            elif choice == "3":
                self.return_book()
            elif choice == "4":
                self.display_available_books()

            elif choice == "5":
                print("Exit The Library System")
                break
            else:
                print("Invalid input Please try again")

if __name__ == "__main__":
    library = Library()
    library.run_library()

'''
 3. Expense Tracker
 Objective:
 Build a program that helps users track their expenses by categorizing and displaying
 them.
 Requirements:
  User scan add expenses (amount, category, date).
  View total expenses by category.
  Display monthly expense summaries.
  Ensure proper exception handling for invalid entries.
 HowIt Works:
  The program asks users to enter expenses under categories like food, transport,
 rent, entertainment, etc.
 Users can later view total spending per category and a breakdown of monthly
 expenses.
  The system prevents negative values or invalid data entries.
 '''
from datetime import datetime
class Expense:
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date

    def __str__(self):
        return f"Date: {self.date.strtime('%Y-%m-%d %H:%M:%S')}, Category: {self.category}, Amount: R{self.amount:.2f}"

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self):
        try:
            amount = float(input("Please enter your amount: "))
            if amount <= 0:
                print("Amount must be positive ")
                return
            category = input("Enter Category: ")
            date_str = input("Enter Date(YYYY-MM-DD: ")
            date = datetime.strptime(date_str, "%Y-%m-%d")
            expense = Expense(amount ,category, date)
            self.expenses.append(expense)
            print("Expense added successful ")
        except ValueError:
            print("Invalid input please enter valid amount and date (YYYY-MM-DD).")
        except Exception as e:
            print(f"Error occurred: {e}")

    def view_expense_by_category(self):
        category_total = {}
        for expense in self.expenses:
            if expense.category in category_total:
                category_total[expense.category] += expense.amount
            else:
                category_total[expense.category] = expense.amount

        if not category_total:
            print("No expense recorded yet")
        else:
            print("\nExpense by Category: ")
            for category, total in category_total.items():
                print(f"{category}: R{total:.2f}")

    def view_monthly_salary(self):
        monthly_expense = {}
        for expense in self.expenses:
            month_year = expense.date.strftime("%Y-%m")
            if month_year in monthly_expense:
                if expense.category in monthly_expense[month_year]:
                    monthly_expense[month_year][expense.category] += expense.amount
                else:
                    monthly_expense[month_year][expense.category] = expense.amount
            else:
                monthly_expense[month_year] = {expense.category: expense.amount}
        if not monthly_expense:
            print("No expenses recorded yet.")
            return

        print("\nMonthly Expense Summary")
        for month_year,category_total in monthly_expense.items():
            print(f"\n{month_year}: ")
            for category, total in category_total.items():
                print(f" - {category}: R{total:.2f}")

    def expense_run(self):
        while True:
            print("\nExpense Tracker")
            print("1. Add Expense")
            print("2. View Expenses by Category")
            print("3. View monthly Summary")
            print("4. Exit")

            choice = input("Enter Choice: ")

            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_expense_by_category()
            elif choice == "3":
                self.view_monthly_salary()
            elif choice == "4":
                print("Exiting Expenses Tracker")
                break
            else:
                print("Invalid choice.Please try again")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.expense_run()

'''
 4. Inventory Management System
 Objective:
 Create a program to track inventory in a store by managing stock levels.
 Requirements:
  User scan add new products (name, quantity, price).
  User scan update stock (increase or decrease quantity).
  Allow viewing of all products and their available quantities.
  Notify when a product is out of stock.
  Implement exception handling for invalid operations (e.g., removing more stock
 than available).
 HowIt Works:
  The program maintains a list of products with details like name, quantity, and
 price.
  Users can update stock levels whenever new inventory arrives or when items are
 sold.
  If an item is out of stock, the system prevents further sales until it is restocked.
 '''
class Product:
    def __init__(self,name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"Name: {self.name}, Quantity: {self.quantity}, Price: R{self.price:.2f}"

class InventoryManagementSystem:
    def __init__(self):
        self.products = []

    def add_product(self):
        try:
            name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))

            if quantity < 0 or price < 0:
                print("Quantity and price must be non-negative")
                return
            product = Product(name, quantity, price)
            self.products.append(product)
            print("Product added Successfully")
        except ValueError:
            print("Quantity must be an integer and price must be a number")
        except Exception as e:
            print(f"An error occurred {e}")

    def update_stock(self, increase=True):
        try:
            name = input("Enter a product name to update: ")
            quantity_change = int(input("Enter quantity to add/remove"))
            if quantity_change == 0:
                print("Change must be non zero integer")
                return
            for product in self.products:
                if product.name == name:
                    if increase:
                        product.quantity += quantity_change
                    else:
                        if product.quantity - quantity_change < 0:
                            print("Not enough stock available")
                            return
                        product.quantity -= quantity_change
                        print("Stock updated successfully")

                        if product.quantity == 0:
                            print(f"{product.name} is out of stock" )
                            return
                        print("Product not found")
        except ValueError:
            print("Invalid input. Quantity must be an integer")
        except Exception as e:
            print(f"An error occurred: {e}")

    def remove_stock(self):
        self.update_stock(increase=False)

    def view_all_product(self):
        if not self.products:
            print("No product in the Inventory")
        else:
            print("Inventory")
            for product in self.products:
                print(product)

    def run_inventory(self):
        while True:
            print("\nInventory Management System")
            print("1. Add Product")
            print("2. Update Stock (Add)")
            print("3. Remove Stock (Subtract)")
            print("4. View all products")
            print("5. exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_product()
            elif choice == "2":
                self.update_stock()
            elif choice == "3":
                self.remove_stock()
            elif choice == "4":
                self.view_all_product()
            elif choice == "5":
                print("Existing Inventory Management System")
                break
            else:
                print("Invalid choice try again")

if __name__ == "__main__":
    ims = InventoryManagementSystem()
    ims.run_inventory()


'''
 5. Mini Calculator App
 Objective:
 Develop a calculator that performs basic arithmetic operations.
 Requirements:
  Support addition, subtraction, multiplication, and division.
  User scan enter two numbers and select an operation.
  Prevent division by zero using exception handling.
  Allow users to perform multiple calculations until they choose to exit.
 HowIt Works:
  The user is prompted to enter two numbers and select an operation (+,-, *, /).
  The program performs the calculation and displays the result.
  If the user enters an invalid input (e.g., dividing by zero), an error message
 appears.
 
'''
def min_calculator_app(num1, num2, operation):
    if operation == "+":
        return num1 + num2

    elif operation == "-":
        return num1 - num2

    elif operation == "*":
        return num1 * num2

    elif operation == "/":
        if num2 == 0:
            raise
        ZeroDivisionError("Cannot divided by Zero")
        return num1 / num2
    else:
        raise
ValueError("Invalid operation")

def min_calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Enter Operation (+,-,/,*): ")
            result_op = min_calculator_app(num1, num2, operation)
            print(f"Results: {result_op}")
        except ValueError as  e:
            print(f"Invalid input. {e}")
        except ZeroDivisionError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred {e}")

        another_calculator = input("Do another calculator (yes/no): ")
        if another_calculator.lower() != "yes":
            break

    print("Calculator existing")
if __name__ == "__main__":
    min_calculator()

'''
6. Hangman Game
 Objective:
 Create a word-guessing game where the player tries to guess a hidden word letter by
 letter before running out of attempts.
 Requirements:
  Select a random word from a predefined list.
  Display the word as underscores (_ _ _ _) where each underscore represents a
 letter.
  Allow the player to guess one letter at a time.
  If the letter is in the word, reveal its position(s).
  If the letter is incorrect, decrease the number of attempts.
  The game ends when the player either:
 o Guesses the word correctly
 o Runs out of attempts ❌
 HowIt Works:
  The program selects a random word (e.g., "PYTHON" → _ _ _ _ _ _).
  The player enters letters one by one.
  If"O"is guessed, the display updates (_ _ _ O _ _).
  If the player guesses wrong, they lose an attempt.
  The game continues until they win or run out of guesses.
 Bonus Features (Optional Enhancements):
  Add a list of words and randomly select one.
  Show the number of attempts left after each wrong guess.
  Keep track of previous guesses to prevent duplicates.
  Draw a visual hangman (stick figure) for each wrong guess
'''

import random
def hangman():
    words = ["PYTHON","HANGMAN","COMPUTER","DEVELOPER","PROGRAMMING",]
    words_to_guess = random.choice(words)
    guess_letter = set()
    attempts = 6
    word_to_display = [ "_" for _ in words_to_guess]
    print("\nWelcome to Hangman")
    while attempts > 0 and "_" in word_to_display:
        print("\nCurrent word: " + "".join(word_to_display))
        print(f"Attempts: {attempts}")
        print(f"Guessed letters: {','.join(sorted(guess_letter))}")

        guess = input("Guess a letter: ").upper()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter")
            continue

        guess_letter.add(guess)

        if guess in words_to_guess:
            print(f"Good guess!! '{guess}' is in the word")
            for index, letter in enumerate(words_to_guess):
                if letter == guess:
                    word_to_display[index] = guess
                else:
                    attempts -= 1
                    print(f"Sorry '{guess}' is not in the word")

    if "_" not in word_to_display:
        print("\nCongratulations!! you've guessed the word: " + words_to_guess)
    else:
        print("\n Game Over!! The word was: " + words_to_guess)

if __name__ == "__main__":
    hangman()
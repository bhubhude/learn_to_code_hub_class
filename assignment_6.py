# --------------------------Beginner--------------------------------#

# 1.Define a class called Person with attributes name and age. Create an instance and print the details.
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name} you are {self.age} years old"

p = Person("Admire Ncube", 39)
d = Person("Reokelitswe Nyathi", 27)
print(p)
print(d)

# 2.Create a class Rectangle with attributes length and width and a method to calculate area.
class Rectangle:

    def __init__(self, length, width ):
        self.length = length
        self.width = width

    def calculate_area(self) -> object:
        return  self.length * self.width

    def __str__(self):
        return f"Rectangle Length :{self.length} Width : {self.width}, Area {self.calculate_area()}"

r1 = Rectangle(17,10)
r2= Rectangle(8,3)
r3 = Rectangle(12,9)
area = r1.calculate_area()
area1 = r2.calculate_area()
area2 = r3.calculate_area()
print(r1)
print(r2)
print(r3)

#3. Define a class Student with name and marks. Create multiple instances and display their details.
class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student Name : {self.name}, Marks {self.marks}"

st = Student("Sibusisiwe Mlotshwa", 37)
st1 = Student("Nobukhosi Moyo", 65)
st2 = Student("Fanyana Ngwenya", 45)
st3 = Student("Lindiwe Zikhali", 81)

print(st)
print(st1)
print(st2)
print(st3)
# 4.Write a class Book with attributes title and author. Add a method to display details.
class Book:
    def __init__(self, title, author, year ):
        self.title = title
        self.author = author
        self.year = year

    def display_details(self):
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")
        print(f"Published : {self.year}")

    def __str__(self):
        return f"Book : {self.title} by Author: {self.author} Published : {self.year}"

book = Book("Ukuchitheka Kombuso waBeThwakazi ","Nkalipho Mathema",2018)
book.display_details()
print(book)

# 5.Create a Laptop class with attributes brand, processor, and RAM. Write a method to print specifications.
class Laptop:
    def __init__(self, brand, processor, ram):
        self.brand = brand
        self.processor = processor
        self.ram = ram

    def specifications(self):
        print(f"Brand : {self.brand}")
        print(f"Processor : {self.processor}")
        print(f"Ram : {self.ram} GB")

    def __str__(self):
        return f"Laptop Brand : {self.brand} Processor : {self.processor} Ram : {self.ram}"

laptop = Laptop("Acer", "Intel", 16)
laptop.specifications()
print(laptop)


#  #-------------------------------Intermediate Questions----------------------------------#
#
# 1.Create a BankAccount class with deposit and withdrawal methods and a private balance attribute.
class BankAccount:
    def __init__(self):
        self.__balance = 0.0

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: R{amount:.2f}. \nNew Balance: R{self.__balance:.2f}")

        else:
            print("Deposit must be positive")

    def withdrawal(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: R{amount:.2f} \nNew Balance: R{self.__balance:.2f}")

        else:
            print("Withdrawal must be positive  and less than or equal to the balance")

    def get_balance(self):
        return  self.__balance

if __name__ == '__main__':
    account = BankAccount()
    account.deposit(100)
    account.withdrawal(85)
    print(f"Final balance: R{account.get_balance():.2f}")





# 2.Write a Shape class with a method area(). Derive Circle and Rectangle classes and override the method.
import math
class Shape:
    def area(self):
        # pass
        raise NotImplementedError("This method should be overridden by subclass")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return  self.width  * self.height

if __name__ == '__main__':
    circle = Circle(8)
    rectangle = Rectangle(10,15)
    print(f"Area of a Circle is {circle.area(): .2f}")
    print(f"Area of a Rectangle is {rectangle.area()}")


# 3.Define a Vehicle class. Inherit Car and Bike from it and add specific attributes to each.
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model


class Car(Vehicle):
    def __init__(self, make ,model,number_of_wheels, number_of_doors):
        super().__init__(make, model)
        self.number_of_wheels = number_of_wheels
        self.number_of_doors = number_of_doors


class Bike(Vehicle):
    def __init__(self, make, model , type_of_bike, number_of_wheels):
        super().__init__(make,model)
        self.type_of_bike = type_of_bike
        self.number_of_wheels = number_of_wheels


car = Car("Mazda3","Sedan", 4, 4)
bike = Bike("Honda Rebel 500", "2017- present", "Sport bike",2)
print(f" Car :{car.make}, {car.model}, {car.number_of_wheels}, {car.number_of_doors}")
print(f"Bike: {bike.make}, {bike.model}, {bike.type_of_bike}, {bike.number_of_wheels}")
# 4.Implement a ShoppingCart class with methods to add and remove items.
class Shopping:
    def __init__(self):
        self.items = {}

    def add_item(self, item,price):
        if item in self.items:
            self.items[item] += price

        else:
            self.items[item] = price
        print(f"Added {item} for R{price:.2f}")

    def remove_item(self,item):
        if item in self.items:
            del self.items[item]
            print(f"Removed {item}")

        else:
            print(f" {item} is not found in the list")

    def total(self):
        return sum(self.items.values())

item_list = Shopping()
item_list.add_item("Amazambane",8.99)
item_list.add_item("Ikhabe",1.99)
item_list.add_item("Amaqanda",2.99)
item_list.add_item("Umthunduluka",6.99)
print(f"Total cost R{item_list.total()}")
item_list.remove_item("Ikhabe")
item_list.remove_item("Amazambane")
print(f"Remove items {item_list.total():.2f}")

# 5.Create a class Employee with methods for salary calculations based on experience level.
class Employee:
    def __init__(self, salary ,name, surname):
        self.salary = salary
        self.name = name
        self.surname = surname

    def calculate_salary(self,years_of_experience):
        if years_of_experience < 0:
            raise ValueError("Years of experience cannot be negative")

        elif years_of_experience < 1:
            return self.salary

        elif years_of_experience < 5:
            return self.salary * 1.1

        else:
            return self.salary * 1.2

if __name__ == '__main__':
    employee = Employee( 1000,"Admire", "Ncube")
    employee1 = Employee(900,"Reokelitswe","Nyathi")
    employee2 = Employee(2000, "Asande", "Dube")
    salary_employee = employee.calculate_salary(10)
    salary_employee1 = employee1.calculate_salary(4)
    salary_employee2 = employee2.calculate_salary(20)
    print(f"Salary for {employee.name} {employee.surname} 10 years of Experience is R{salary_employee:.2f}")
    print(f"Salary for {employee.name} {employee.surname} 10 years of Experience is R{salary_employee1:.2f}")
    print(f"Salary for {employee.name} {employee.surname} 20 years of Experience is R{salary_employee2:.2f}")


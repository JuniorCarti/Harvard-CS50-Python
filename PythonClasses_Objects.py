#python  classes and objects
#A Class is like an object constructor, or a "blueprint" for creating objects.
#To create a class, use the keyword class:
#Create a class named MyClass, with a property named x:
class myClass:
    x = 5

#Now we can use the class named MyClass to create objects:
#Create an object named p1, and print the value of x:
p1 = myClass
print(p1.x)

#The __init__() Function
"""The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
To understand the meaning of classes we have to understand the built-in __init__() function.
All classes have a function called __init__(), which is always executed when the class is being initiated.
Use the __init__() function to assign values to object properties, 
or other operations that are necessary to do when the object is being created:"""
#Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Ridge", 23)
print(p1.name)
print(p1.age)

#The __init__() function is called automatically every time the class is being used to create a new object.

class City:
    def __init__(self, name, country, population, governor):
        self.name = name
        self.country = country
        self.population = population
        self.governor = governor

c1 = City("Chepkemoi Magdaline", "Kenya", 560000, "Hassan Joho")
print(c1.name)
print(c1.country)
print(c1.population)
print(c1.governor)


class Student:
    def __init__(self, name, school, course, specialization):
        self.name = name
        self.school = school
        self.course = course
        self.specialization = specialization
s1 = Student("Ridge", "Eldohub Academy", "CyberSecurity&Networking", "CyberSecurity")
print(s1.name)
print(s1.school)
print(s1.course)
print(s1.specialization)

class Phones:
    def __init__(self, name, brand, date_of_manufacture, operating_system, Manufacturers_name):
        self.name = name
        self.brand = brand
        self.date_of_manufacture = date_of_manufacture
        self.operating_system = operating_system
        self.Manufacturers_name = Manufacturers_name
Ph1 = Phones("Samsung S24", "Samsung", 2024, 14.0, "Samsung Knox")
print(Ph1.name)
print(Ph1.brand)
print(Ph1.date_of_manufacture)
print(Ph1.operating_system)
print(Ph1.Manufacturers_name)

class Courses:
    def __init__(self, name, fee, duration_of_course, school_offered, cut_outPoints):
        self.name = name
        self.fee = fee
        self.duration_of_course = duration_of_course
        self.school_offered = school_offered
        self.cut_outPoints = cut_outPoints
Cr1 = Courses("Diploma in Electrical Engineering", 56000, 3, "Eldoret Polytechnic", 56)
print(f"The name of the course is: {Cr1.name}")

#The __str__() Function
#The __str__() function controls what should be returned when the class object is represented as a string.
#If the __str__() function is not set, the string representation of the object is returned:
#The string representation of an object WITHOUT the __str__() function:
class Courses:
    def __init__(self, name, fee, duration_of_course, school_offered, cut_outPoints):
        self.name = name
        self.fee = fee
        self.duration_of_course = duration_of_course
        self.school_offered = school_offered
        self.cut_outPoints = cut_outPoints
Cr1 = Courses("Diploma in Electrical Engineering", 56000, 3, "Eldoret Polytechnic", 56)
print(Cr1)
#You will get an error

#The string representation of an object WITH the __str__() function:
class Courses:
    def __init__(self, name, fee, duration_of_course, school_offered, cut_outPoints):
        self.name = name
        self.fee = fee
        self.duration_of_course = duration_of_course
        self.school_offered = school_offered
        self.cut_outPoints = cut_outPoints
        
    def __str__(self):
        return f"Your course is: {self.name}\nYou will pay a total fee of: {self.fee}$ \nThe Duration of the course is: {self.duration_of_course} years\nYou will be enrolled at: {self.school_offered}\nYour cut out points of  {self.cut_outPoints} qualify you to enroll"
Cr1 = Courses("Diploma in Electrical Engineering", 56000, 3, "Eldoret Polytechnic", 56)

print(Cr1)


#Object Methods
#Objects can also contain methods. Methods in objects are functions that belong to the object.
#Let us create a method in the Courses class:
class Courses:
    def __init__(self, name, fee, duration_of_course, school_offered, cut_outPoints):
        self.name = name
        self.fee = fee
        self.duration_of_course = duration_of_course
        self.school_offered = school_offered
        self.cut_outPoints = cut_outPoints
        
    def myfunc(self):
        print("Congratulations Ridge on your enrollment to " + self.name)

Cr1 = Courses("Diploma in Electrical Engineering", 56000, 3, "Eldoret Polytechnic", 56)
Cr1.myfunc()  

#The self Parameter
#The self parameter is a reference to the current instance of the class, 
#and is used to access variables that belong to the class.
#It does not have to be named self, you can call it whatever you like, 
# but it has to be the first parameter of any function in the class:

#now lets use the word eldoret and ridge instead of self 

class Courses:
    def __init__(eldoret, name, fee, duration_of_course, school_offered, cut_outPoints):
        eldoret.name = name
        eldoret.fee = fee
        eldoret.duration_of_course = duration_of_course
        eldoret.school_offered = school_offered
        eldoret.cut_outPoints = cut_outPoints
        
    def myfunc(ridge):
        print("Congratulations Ridge on your enrollment to " + ridge.name)

Cr1 = Courses("Diploma in Electrical Engineering", 56000, 3, "Eldoret Polytechnic", 56)
Cr1.myfunc() 

#Modify Object Properties
#You can modify properties on objects like this:
Cr1.fee = 60000
print(f"Next Term Fee is: {Cr1.fee}")

#Delete Object Properties
#You can delete properties on objects by using the del keyword:
#example del the fee property
#del Cr1.fee
#print(Cr1.fee) you will get an error since the property has been deleted

#Delete Objects
#You can delete objects by using the del keyword:
#Delete the Cr1 object

#The pass Statement
#class definitions cannot be empty, but if you for some reason have a class definition with no content,
# put in the pass statement to avoid getting an error.

class Laptops:
    pass

#Examples of real scenarios
#1. Bank Account System

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New Balance: ${self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds!")
        else:
            self.balance -= amount
        print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")

    def __str__(self):
        return f"Account Holder: {self.account_holder} \nBalance: ${self.balance}"
    
    # create an account
account1 = BankAccount("Ridge", 1000)
print(account1) # uses __str__
    
account1.deposit(500) # method call
account1.withdraw(200)
    
    # Modify balance
account1.balance = 2000
print(f"Updated Balance: ${account1.balance}")
    

#smartphone inventory
class Smartphone:
     def __init__(self, model, brand, price, os):
        self.model = model
        self.brand = brand
        self.price = price
        self.os = os
     def apply_discount(self, discount):
        self.price *= (1 - discount/100)
        print(f"Discounted price: ${self.price:.2f}")
     def __str__(self):
        return f"{self.brand} {self.model} (OS: {self.os}) - ${self.price}"
     
# Create a phone
phone1 = Smartphone("iPhone 15", "Apple", 999, "iOS 17")
print(phone1)  # Uses __str__

phone1.apply_discount(10)  # 10% discount
# Modify OS
phone1.os = "iOS 18 Beta"
print(f"Updated OS: {phone1.os}")


#student enrollment system

class Student:
    def __init__(self, name, course, gpa):
        self.name = name
        self.course = course
        self.gpa = gpa
    def promote(self):
        if self.gpa >= 3.0:
            print(f"{self.name} is promoted to the next semester!")
        else:
            print(f"{self.name} needs to repeat.")
    def __str__(self):
        return f"Student: {self.name}\nCourse: {self.course}\nGPA: {self.gpa}"

# Enroll a student
student1 = Student("Alice", "Computer Science", 3.5)
print(student1)  # Uses __str__

student1.promote()  # Method call

# Update GPA
student1.gpa = 2.9
student1.promote()  # Re-evaluate

# E-Commerce Product Management
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    def restock(self, quantity):
        self.stock += quantity
        print(f"Restocked {quantity} units. Total stock: {self.stock}")
    def __str__(self):
        return f"Product: {self.name}\nPrice: ${self.price}\nStock: {self.stock}"
    

# Add a product
product1 = Product("Wireless Earbuds", 59.99, 100)
print(product1)  # Uses __str__

product1.restock(50)  # Method call

# Change price
product1.price = 49.99  # Price drop
print(f"New price: ${product1.price}")
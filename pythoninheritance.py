#Python Inheritance
#Inheritance allows us to define a class that inherits all the methods and properties from another class.
#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class, also called derived class.
#Create a Parent Class
#Any class can be a parent class, so the syntax is the same as creating any other class:

#create a class named Person with firstname and lastname properties and a print method
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname) 
#Use the Person class to create an object, and then execute the printname method:
x = Person("Ridge", "Junior")
x.printname()

#Create a Child Class
#To create a class that inherits the functionality from another class, 
#send the parent class as a parameter when creating the child class:
#Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(Person):
  pass

#Note: Use the pass keyword when you do not want to add any other properties or methods to the class.
#Use the Student class to create an object, and then execute the printname method:
x = Student("Thiak", "Ayuen")
x.printname()

#Add the __init__() Function
#We want to add the __init__() function to the child class (instead of the pass keyword).
#Note: The __init__() function is called automatically every time the class is being used to create a new object.
#Add the __init__() function to the Student class:
class Student(Person):
  def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

#use the super function

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
#By using the super() function, you do not have to use the name of the parent element, 
#it will automatically inherit the methods and properties from its parent.
#Add Properties
#Add a property called graduationyear to the Student class:
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

#Add a year parameter, and pass the correct year when creating objects:
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

#Add Methods
#Add a method called welcome to the Student class:
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
    
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
#Python Conditions and If statements
#Python supports the usual logical conditions from mathematics:
#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b

a=33
b=45

if a < b:
    print("a is less than b")

#Elif
#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
a=33
b=45

if a < b:
    print("a is less than b")
elif a >= b:
    print("b is greater than a")

#else keyword
#The else keyword catches anything which isn't caught by the preceding conditions.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#In this example a is greater than b, so the first condition is not true, 
# also the elif condition is not true, so we go to the else condition and print to screen that "a is greater than b".

#You can also have an else without the elif:
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Short Hand If
#If you have only one statement to execute, you can put it on the same line as the if statement.
if a > b: print("a is greater than b")

#Short Hand If ... Else
#If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
a = 2
b = 330
print("A") if a > b else print("B")
#This technique is known as Ternary Operators, or Conditional Expressions.
#You can also have multiple else statements on the same line:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#And keyword
#The and keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#Or keyword
#The or keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#Not keyword
#The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#Nested If
#You can have if statements inside if statements, this is called nested if statements.
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#The pass Statement
#if statements cannot be empty, 
# but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a:
  pass

#Basic If Statement
# Syntax
# if condition:
#     # code to execute if condition is True

# Example
temperature = 30
if temperature > 25:
    print("It's a hot day!")

#If-Else Statement
#Adds an alternative path when the condition is false.
# Syntax
# if condition:
#     # code if True
# else:
#     # code if False

# Example
age = 17
if age >= 18:
    print("You can vote!")
else:
    print("You cannot vote yet.")

# Login system
#password = "secret123"
#input_password = input("Enter password: ")

#if input_password == password:
 #   print("Access granted")
#else:
 #   print("Access denied")

#If-Elif-Else Statement
#Handles multiple conditions in sequence.
"""# Syntax
if condition1:
    # code if condition1 is True
elif condition2:
    # code if condition2 is True
else:
    # code if all above are False"""

score = 85
if score >= 90:
   grade = "A"
elif score >= 80:
   grade = "B"
elif score >= 70:
   grade = "C"
else:
   grade = "F"
print(f"Your grade is {grade}")

#shipping cost calculator
weight = 4.5  # in kg
if weight <= 2:
    cost = 5
elif weight <= 5:
    cost = 10
elif weight <= 10:
    cost = 15
else:
    cost = 20
print(f"Shipping cost: ${cost}")

#Nested If Statements
#If statements inside other if statements.
# Example
num = 15
if num > 0:
    print("Positive number")
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Non-positive number")

# Movie ticket pricing
age = 25
is_student = True

if age < 5:
    price = 0  # free for young children
else:
    if age < 18:
        price = 8  # child price
    elif age >= 65:
        price = 7  # senior price
    else:
        if is_student:
            price = 9  # student price
        else:
            price = 12  # adult price
print(f"Ticket price: ${price}")

#Ternary Operator (Conditional Expression)
#A concise way to write simple if-else statements.
# Syntax
#value_if_true if condition else value_if_false

# Example
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)

# Discount eligibility
purchase_amount = 120
discount = 0.1 if purchase_amount > 100 else 0
final_amount = purchase_amount * (1 - discount)
print(f"Final amount: ${final_amount:.2f}")

#Boolean Conditions and Comparisons
"""Conditions can use various comparison operators:
== equal to
!= not equal to
> greater than
< less than
>= greater than or equal to
<= less than or equal """
# Example with multiple conditions
temperature = 22
is_weekend = True

if temperature > 25 and is_weekend:
    print("Great day for the beach!")
elif temperature > 25 or is_weekend:
    print("Good day to go outside")
else:
    print("Maybe stay indoors")

#Logical Operators
#Combine conditions with and, or, not.
# Example
has_ticket = True
has_id = True
age = 19

if has_ticket and (has_id and age >= 18):
    print("You can enter the club")
else:
    print("Entry denied")

# Loan approval
credit_score = 720
income = 50000
employment_years = 2

if (credit_score >= 700) and (income >= 40000 or employment_years > 1):
    print("Loan approved!")
else:
    print("Loan denied")

#Special Cases and Edge Conditions
"""Truthy and Falsy Values
In Python, these values are considered False in boolean context:
False
None
Zero of any numeric type (0, 0.0, 0j)
Empty sequences ('', [], ())
Empty mappings ({})
All other values are considered True"""
# Example
name = ""
if name:
    print(f"Hello, {name}!")
else:
    print("Hello, stranger!")

# Checking for empty input
user_input = input("Enter your feedback: ")
if user_input.strip():  # checks if input is not empty after removing whitespace
    print("Thank you for your feedback!")
else:
    print("Please provide some feedback")


#1. User Authentication System
username = 'admin'
password = 'user1234'
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    input_user = input("Username: ")
    input_pass = input("Password: ")
    if input_user == username and input_pass == password:
        print("Login successful!")
        break
    elif input_user != username and input_pass != password:
       print("Enter correct username!")
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Invalid credentials. {remaining} attempts remaining.")
        else:
            print("Account locked. Contact administrator.")

#2. Temperature Alert System
temperature = float(input("Enter current temperature in Celsius: "))
humidity = float(input("Enter current humidity percentage: "))

if temperature > 30:
    if humidity > 70:
        print("DANGER: Extreme heat and humidity! Stay indoors.")
    else:
        print("WARNING: Hot day! Stay hydrated.")
elif temperature < 0:
    print("WARNING: Freezing temperatures! Dress warmly.")
elif 20 <= temperature <= 25 and 40 <= humidity <= 60:
    print("Perfect weather conditions!")
else:
    print("Normal weather conditions.")
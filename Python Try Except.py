#The try block lets you test a block of code for errors.
#The except block lets you handle the error.
#The else block lets you execute code when there is no error.
#The finally block lets you execute code, regardless of the result of the try- and except blocks.
#Exception Handling
try:
  print(x)
except:
  print("An exception occurred")

  #Many Exceptions
  #You can define as many exception blocks as you want, 
  #e.g. if you want to execute a special block of code for a special kind of error:
  #Print one message if the try block raises a NameError and another for other errors:
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

  #Else
  #You can use the else keyword to define a block of code to be executed if no errors were raised:

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

#Finally
#The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

#Try to open and write to a file that is not writable:
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

#Raise an exception
#As a Python developer you can choose to throw an exception if a condition occurs.
#To throw (or raise) an exception, use the raise keyword.
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

#The raise keyword is used to raise an exception.
#You can define what kind of error to raise, and the text to print to the user.
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")

#Example 1: Catching a specific error
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter a valid number.")

#Example 2: Catching all errors (not recommended for production)
try:
    x = 5 / 0
except Exception as e:
    print(f"An error occurred: {e}")

#Example 3: Using else and finally
try:
    value = int(input("Enter a number: "))
except ValueError:
    print("That was not a number!")
else:
    print(f"You entered {value}")
finally:
    print("This always runs (cleanup, closing files, etc.)")

#1. Reading a File (FileNotFoundError)
try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file was not found. Please check the file name or path.")


# API Call or Internet Request (ConnectionError)
import requests

try:
    response = requests.get("https://example.com/api/data")
    print(response.json())
except requests.exceptions.ConnectionError:
    print("Network connection failed. Check your internet.")
#3. User Input (ValueError, ZeroDivisionError)
try:
    age = int(input("Enter your age: "))
    years_left = 100 - age
    print(f"You have around {years_left} years to 100!")
except ValueError:
    print("You must enter a number.")
except ZeroDivisionError:
    print("Division by zero occurred.")  # unlikely here but just in case

# 4. Banking App – Withdraw Function (Custom Exception)
class InsufficientBalance(Exception):
    pass

balance = 500

def withdraw(amount):
    if amount > balance:
        raise InsufficientBalance("Not enough balance to withdraw.")
    return balance - amount

try:
    new_balance = withdraw(600)
    print("Withdrawal successful. New balance:", new_balance)
except InsufficientBalance as e:
    print(f"Error: {e}")

#5. Writing to a File (PermissionError)
try:
    with open("/root/secret.txt", "w") as file:
        file.write("Top Secret Data")
except PermissionError:
    print("Permission denied. You can't write to this location.")

# 6. Sending an Email (smtplib.SMTPException)
import smtplib

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("your_email@gmail.com", "wrong_password")
    server.sendmail("your_email@gmail.com", "receiver@gmail.com", "Test message")
    server.quit()
except smtplib.SMTPAuthenticationError:
    print("Failed to authenticate. Check your email or password.")
except smtplib.SMTPException as e:
    print(f"SMTP error occurred: {e}")

#Global Variables 
#This file contains all the global variables used in the project
#It is used to store the global variables that are used in the project
#Create a variable outside of a function, and use it inside the function
#Global variables are variables that are declared outside of a function and can be accessed inside the function
#Global variables are declared using the global keyword
#Global variables are used to store data that can be accessed by all functions in the project
#x = "awesome"

#def myfunc():
 # print("Python is " + x)

#myfunc()
#This is a simple example of how to use global variables in Python

x = "awesome"
def myfunc():
    global x
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is " + x)

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
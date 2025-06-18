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
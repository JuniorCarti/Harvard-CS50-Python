#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.
#     return lambda name: f"{greeting}, {name}!"    
#Basic syntax
#lambda arguments: expression
#The expression is executed and the result is returned:
x = lambda a : a + 10
print(x(5))

#Lambda functions can take any number of arguments:
#Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6))

#Summarize argument a, b, and c and return the result:
x = lambda a, b, c : a + b + c
print(x(10, 20, 30))
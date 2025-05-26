#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.
#Sysntax
# lambda arguments: expression
def add(x, y):
    return x + y
add_lambda = lambda x, y: x + y
print(add(5, 3))  # Output: 8
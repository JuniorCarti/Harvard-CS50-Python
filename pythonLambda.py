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

#Why Use Lambda Functions?
#The power of lambda is better shown when you use them as an anonymous function inside another function.
#Say you have a function definition that takes one argument, 
#and that argument will be multiplied with an unknown number:
def myfunc(n):
    return lambda a: a * n

#Use that function definition to make a function that always doubles the number you send in:
mydoubler = myfunc(2)
print(mydoubler(11))

#Or, use the same function definition to make a function that always triples the number you send in:
mytripler = myfunc(3)
print(mytripler(11))

#Or, use the same function definition to make both functions, in the same program:
mydoubler = myfunc(4)
mytripler = myfunc(5)

print(mydoubler(50))
print(mytripler(60))

#sorting with custom keys
# Sorting a list of tuples by the second element
students = [('Alice', 88), ('Bob', 95), ('Charlie', 78)]
students_sorted = sorted(students, key=lambda x: x[1])
print(students_sorted)
# Output: [('Charlie', 78), ('Alice', 88), ('Bob', 95)]

#2. Filtering Data
# Filtering even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
# Output: [2, 4, 6, 8]
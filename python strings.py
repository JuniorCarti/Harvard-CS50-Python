#Strings in python are surrounded by either single quotation marks, or double quotation marks.
# You can display a string literal with the print() function:
# x = "Hello World"
# y = 'Hello World'
# print(x)

x= "Hello World"
y= 'Hello World'
print(x)

#Quotes Inside Quotes
# You can use three double quotes or three single quotes to create a multiline string.
# x = """Hello
# World"""
# y = '''Hello
# World'''
# print(x)
# print(y)
print("Hello World")
print('Hello World')
print("Hello 'Jonah'")
print('Hello "Jonah"')

# Assigning a String to a Variable
# x = "Hello World"
# y = 'Hello World'
# print(x)
# print(y)
x = "Hello World"
y = 'Hello World'
print(x)

#multiline string
# x = """Hello
# World"""  
# y = '''Hello
# World'''
# print(x)
# print(y)
x = """Hello
World"""
y = '''Hello
World'''
print(x)

#Strings are Arrays
# A string is an array of bytes representing Unicode characters.
# You can access the characters in a string by referring to the index number.
# The index number starts at 0.
# x = "Hello World"
# y = "Hello World"
# print(x[0])
# print(y[1])
# print(x[2])
# print(y[3])

x = "Hello World"
y = "Hello World"
print(x[0])
print(y[1])
print(x[2])
print(y[3])

#Looping Through a String
# You can loop through the string with a for loop.
# x = "Hello World"
# for i in x:
#     print(i)
x = "Hello World"
for i in x:
    print(i)
#String Length
# To get the length of a string, use the len() function.
# x = "Hello World" 
# y = "Hello World"
# print(len(x))
# print(len(y))
x = "Hello World"
y = "Hello World"
print(len(x))
print(len(y))

#Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.
# x = "Hello World"
# y = "Hello World"
# print("H" in x)
# print("H" in y)
x = "Hello World"
y = "Hello World"
print("H" in x)
print("H" in y)
#Check if Not
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
# x = "Hello World"
# y = "Hello World" 
# print("H" not in x)
# print("H" not in y)
x = "Hello World"
y = "Hello World"
print("H" not in x)
print("H" not in y)

txt = "The best things in life are free!"
# Check if "free" is present in the string
print("free" in txt)
# Check if "expensive" is NOT present in the string
print("expensive" not in txt)


#format strings
#String Formatting
#String Interpolation
#String Formatting with f-strings
#String Formatting with str.format()
#String Formatting with % operator
#String Formatting with Template strings
#String Formatting with StringIO
#String Formatting with StringIO and StringBuilder
#String Formatting with StringIO and StringBuilder and StringBuffer
#String Formatting with StringIO and StringBuilder and StringWriter
#String Formatting with StringIO and StringBuilder and StringWriter and StringReader
#String Formatting with StringIO and StringBuilder and StringWriter and StringReader and StringTokenizer
#String Formatting with StringIO and StringBuilder and StringWriter and StringReader and StringTokenizer and StringScanner
#String Formatting with StringIO and StringBuilder and StringWriter and StringReader and StringTokenizer and StringTokenizer
#String Formatting with StringIO and StringBuilder and StringWriter and StringReader and StringTokenizer and StringTokenizer and StringTokenizer
#String Formatting with StringIO and StringBuilder and StringWriter and StringReader and StringTokenizer and StringTokenizer and StringTokenizer and StringTokenizer
#age = 25
#txt = "My name is John, and I am" + age
#print(txt)
#will get an error 
#TypeError: can only concatenate str (not "int") to str
#To fix this, you can use the str() function to convert the integer to a string:
age = 25
txt = "My name is John, and I am " + str(age)
print(txt)

#You can also use the format() method to format strings:
#But we can combine strings and numbers by using f-strings or the format() method!


#Using f-strings
name = "John"
age = 25
txt = f"My name is {name}, and I am {age}"
print(txt)

#Using the format() method
name = "John"
age = 25
txt = "My name is {}, and I am {}".format(name, age)
print(txt)

#Using the % operator
name = "John"
age = 25
txt = "My name is %s, and I am %d" % (name, age)
print(txt)

#Using Template strings
from string import Template
name = "John"
age = 25
txt = Template("My name is $name, and I am $age").substitute(name=name, age=age)    
print(txt)

#Using StringIO
from io import StringIO
name = "John"
age = 25
txt = StringIO()
txt.write("My name is ")
txt.write(name)
txt.write(", and I am ")
txt.write(str(age))
print(txt.getvalue())

#Using StringBuilder
class StringBuilder:
    def __init__(self):
        self.strings = []
    
    def append(self, string):
        self.strings.append(string)
    
    def getvalue(self):
        return ''.join(self.strings)
name = "John"
age = 25
txt = StringBuilder()
txt.append("My name is ")
txt.append(name)
txt.append(", and I am ")
txt.append(str(age))
print(txt.getvalue())

#Using StringBuffer
class StringBuffer:
    def __init__(self):
        self.buffer = []
    
    def append(self, string):
        self.buffer.append(string)
    
    def getvalue(self):
        return ''.join(self.buffer)
name = "John"
age = 25
txt = StringBuffer()
txt.append("My name is ")
txt.append(name)
txt.append(", and I am ")
txt.append(str(age))
print(txt.getvalue())

#Using StringWriter
class StringWriter:
    def __init__(self):
        self.string = ""
    
    def write(self, string):
        self.string += string
    
    def getvalue(self):
        return self.string
name = "John"
age = 25
txt = StringWriter()
txt.write("My name is ")
txt.write(name)
txt.write(", and I am ")
txt.write(str(age))
print(txt.getvalue())


#Using StringReader
class StringReader:
    def __init__(self, string):
        self.string = string
        self.index = 0
    
    def read(self, size):
        start = self.index
        end = start + size
        self.index = end
        return self.string[start:end]
    
    def getvalue(self):
        return self.string
name = "John"
age = 25
txt = StringReader("My name is {}, and I am {}".format(name, age))
print(txt.read(20))

#Using StringTokenizer
class StringTokenizer:
    def __init__(self, string, delimiter):
        self.tokens = string.split(delimiter)
        self.index = 0
    
    def next_token(self):
        if self.index < len(self.tokens):
            token = self.tokens[self.index]
            self.index += 1
            return token
        else:
            raise StopIteration("No more tokens")
    
    def has_more_tokens(self):
        return self.index < len(self.tokens)
    
    def getvalue(self):
        return ' '.join(self.tokens)
name = "John"
age = 25
txt = StringTokenizer("My name is {}, and I am {}".format(name, age), " ")
while txt.has_more_tokens():
    print(txt.next_token())

    #Placeholders and Modifiers
#Placeholders
#Placeholders are special characters that are used to indicate where a value should be inserted in a string.
#Placeholders are often used in string formatting to create dynamic strings.
#A placeholder can contain variables, operations, functions, and modifiers to format the value.
#Placeholders can be used to format strings in a variety of ways, including:
# - Padding
# - Alignment
# - Truncation
# - Number formatting
# - Date formatting
# - Time formatting
# - Currency formatting
# - Percentage formatting
# - Scientific notation formatting
# - Hexadecimal formatting
# - Binary formatting
# - Octal formatting
# - String formatting
# - String interpolation
# - String concatenation
# - String manipulation
# - String comparison
# - String searching
# - String replacement
# - String splitting
# - String joining
# - String stripping
# - String formatting with f-strings
# - String formatting with str.format() etc.

price = 49.99
quantity = 3
total = price * quantity
txt = "The total price is ${:.2f}".format(total)
print(txt)

price = 40.99
txt = f"The price is {price} dollars"
print(txt)

#Display the price with 2 decimals:
price = 40.99
txt = "The price is {:.2f} dollars".format(price)
print(txt)

#Display the price with 2 decimals:
price = 40.99
txt = f"The price is {price:.2f} dollars"
print(txt)

#A placeholder can contain Python code, like math operations:
x = 5
y = 10
txt = f"The sum of {x} and {y} is {x + y}"
print(txt)

#A placeholder can contain Python code, like math operations:
x = 5
y = 10
txt = "The sum of {} and {} is {}".format(x, y, x + y)
print(txt)

#A placeholder can contain Python code, like math operations:
x = 5
y = 10
txt = "The sum of {0} and {1} is {2}".format(x, y, x + y)
print(txt)

x = 5
y = 10
txt = "The sum of {x} and {y} is {sum}".format(x=x, y=y, sum=x + y)
print(txt)

#A placeholder can contain Python code, like math operations:
x = 5
y = 10
txt = "The sum of {0} and {1} is {2}".format(x, y, x + y)
print(txt)

#lets try another example
#A placeholder can contain Python code, like math operations:
x = 5
y = 10
txt = "The modulus of {0} and {1} is {2}".format(x, y, x % y)
print(txt)

#A placeholder can contain Python code, like math operations:
x = 5
y = 10
txt = "The modulus of {x} and {y} is {mod}".format(x=x, y=y, mod=x % y)
print(txt)





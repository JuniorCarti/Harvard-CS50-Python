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



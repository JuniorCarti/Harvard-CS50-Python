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


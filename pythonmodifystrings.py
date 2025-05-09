#Python has a set of built-in methods that you can use on strings.
#Upper Case
#The upper() method returns the string in upper case
#x = "Hello World"
#y = "Hello World"
x = "Hello World"
y = "Hello World"
print(x.upper())
print(y.upper())

#Lower Case
#The lower() method returns the string in lower case
#x = "Hello World"
#y = "Hello World"
x = "Hello World"
y = "Hello World"
print(x.lower())
print(y.lower())

#Remove Whitespace
#The strip() method removes any whitespace from the beginning or the end of a string        
#x = " Hello World "
#y = " Hello World "
x = " Hello World "
y = " Hello World "
print(x.strip())
print(y.strip())
#The lstrip() method removes any whitespace from the beginning of a string
#x = " Hello World "
#y = " Hello World "
x = " Hello World " 
y = " Hello World "
print(x.lstrip())
print(y.lstrip())

#The rstrip() method removes any whitespace from the end of a string
#x = " Hello World "
#y = " Hello World "
x = " Hello World "
y = " Hello World "
print(x.rstrip())
print(y.rstrip())

#Replace String
#The replace() method replaces a string with another string
#x = "Hello World"
#y = "Hello World"
x = "Hello World"
y = "Hello World"
print(x.replace("H", "J"))
print(y.replace("H", "D"))
#The split() method splits a string into a list
#x = "Hello World"
#y = "Hello World"
x = "Hello World"   
y = "Hello World"
print(x.split())
print(y.split())

#The join() method joins the elements of a list into a string
#x = ["Hello", "World"]
#y = ["Hello", "World"]
x = ["Hello", "World"]
y = ["Hello", "World"]
print(" ".join(x))
print(" ".join(y))
#The find() method finds a specified value in a string
#x = "Hello World"
#y = "Hello World"
x = "Hello World"
y = "Hello World"
print(x.find("H"))
print(y.find("H"))
#The index() method finds a specified value in a string
#x = "Hello World"
#y = "Hello World"
x = "Hello World"
y = "Hello World"
print(x.index("H"))
print(y.index("H"))
#The count() method returns the number of times a specified value occurs in a string
#x = "Hello World"
#y = "Hello World"
x = "Hello World"
y = "Hello World"
print(x.count("H"))
print(y.count("H"))
print(x.count("l"))
print(y.count("l"))

#The startswith() method returns True if the string starts with the specified value
#x = "Hello World"
#y = "Hello World"
x = "Hello World"
y = "Hello World"
print(x.startswith("H"))
print(y.startswith("H"))

#The endswith() method returns True if the string ends with the specified value
#x = "Hello World"
#y = "Hello World"
x = "Hello World"
y = "Hello World"
print(x.endswith("d"))
print(y.endswith("d"))
print(x.endswith("H"))
print(y.endswith("H"))

#The isalnum() method returns True if all characters in the string are alphanumeric
#x = "Hello World"
#y = "Hello World"
x = "Hello World"
y = "Hello World"
print(x.isalnum())
print(y.isalnum())

#The isalpha() method returns True if all characters in the string are alphabetic
#x = "Hello World"
#y = "Hello World"
x = "Hello World"
y = "Hello World"
print(x.isalpha())
print(y.isalpha())

#The isdigit() method returns True if all characters in the string are digits
#x = "Hello World"
#y = "Hello World"
x = "Hello World"
y = "Hello World"
print(x.isdigit())
print(y.isdigit())

#The islower() method returns True if all characters in the string are lower case
#x = "Hello World"
#y = "Hello World"
x = "hello world"
y = "Hello World"
print(x.islower())
print(y.islower())

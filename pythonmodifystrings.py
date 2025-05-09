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

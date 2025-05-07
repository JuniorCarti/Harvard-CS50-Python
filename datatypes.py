#Built-in Data Types
# Python has the following built-in data types:
#
# 1. Text Type:	str
# 2. Numeric Types:	int, float
# 3. Sequence Types:	list, tuple, range  
#4. Mapping Type:	dict
# 5. Set Types:	set, frozenset
# 6. Boolean Type:	bool
# 7. Binary Types:	bytes, bytearray, memoryview
# 8. None Type:	NoneType
#
# 9. User-defined Types:	Custom classes and objects
# 10. Enumerations:	Enum classes
# 11. Data Classes:	Dataclasses for creating classes with built-in methods

#Getting the data type of an object
# You can use the type() function to get the data type of an object.
# The type() function returns the type of the object. The type() function is a built-in function in Python that returns the type of an object. It can be used to check the data type of a variable or an expression. The type() function takes one argument, which is the object whose type you want to check. It returns the type of the object as a string.
x = "Hello World"
print(type(x)) # <class 'str'>
x = 20
print(type(x)) # <class 'int'>
x = 20.5
print(type(x)) # <class 'float'>
x = ["apple", "banana", "cherry"]
print(type(x)) # <class 'list'>
x = ("apple", "banana", "cherry")
print(type(x)) # <class 'tuple'>
x = range(5)
print(type(x)) # <class 'range'>
x = {"name": "John", "age": 36}
print(type(x)) # <class 'dict'>
x = {"apple", "banana", "cherry"}
print(type(x)) # <class 'set'>
x = frozenset({"apple", "banana", "cherry"})
print(type(x)) # <class 'frozenset'>
x = True
print(type(x)) # <class 'bool'>
x = b"Hello"
print(type(x)) # <class 'bytes'>
x = bytearray(5)
print(type(x)) # <class 'bytearray'>
x = memoryview(bytes(5))
print(type(x)) # <class 'memoryview
x = None
print(type(x)) # <class 'NoneType'>
x = 5
print(type(x)) # <class 'int'>
x = 5.0
print(type(x)) # <class 'float'>
x = 5 + 2j
print(type(x)) # <class 'complex'>
x = 5.0 + 2j
print(type(x)) # <class 'complex'>


#python numbers
# Python Numbers
# Python has three built-in numeric data types:
# 1. int (integer): Represents whole numbers, both positive and negative, without decimals.
# 2. float (floating-point): Represents real numbers, both positive and negative, with decimals.
# 3. complex: Represents complex numbers, which are numbers with a real and imaginary part.
x = 5
y = 2.5
z = 3 + 4j
print(type(x)) # <class 'int'>
print(type(y)) # <class 'float'>
print(type(z)) # <class 'complex'>

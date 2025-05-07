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
#integer
# An integer is a whole number, positive or negative, without decimals.
# Integers can be of any length, and Python automatically handles large integers.
# Integers can be created using decimal, binary, octal, or hexadecimal notation.
# Decimal: Base 10, e.g., 10, -5
# Binary: Base 2, e.g., 0b1010 (which is 10 in decimal)
# Octal: Base 8, e.g., 0o12 (which is 10 in decimal)
# Hexadecimal: Base 16, e.g., 0xA (which is 10 in decimal)
# Python supports arbitrary-precision integers, meaning you can work with very large numbers without worrying about overflow.
# Python automatically converts large integers to a long type when necessary.
# Python also supports negative integers, which are represented with a minus sign (-) in front of the number.
# Negative integers can be used in mathematical operations just like positive integers.
# Python provides built-in functions for working with integers, such as abs() to get the absolute value, pow() to raise a number to a power, and divmod() to get the quotient and remainder of a division operation.
# Python also supports integer arithmetic, including addition, subtraction, multiplication, and division.
# Integer division can be performed using the // operator, which returns the quotient without the remainder.
# Python also supports the modulo operator % to get the remainder of a division operation.
x = 10
y = -5
print(type(x)) # <class 'int'>
print(type(y)) # <class 'int'>
print(type(0b1010)) # <class 'int'>
print(type(0o12)) # <class 'int'>
print(type(0xA)) # <class 'int'>
print(type(10)) # <class 'int'>
print(type(-5)) # <class 'int'>
print(type(10.5)) # <class 'float'>

#Float
# A float is a number that has a decimal point or is in exponential (scientific) notation.
#Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
# Floats can also be represented in scientific notation, which is a way of expressing very large or very small numbers using powers of 10.
# For example, 1.5e2 represents 1.5 * 10^2, which is equal to 150.0.
# Similarly, 2.5e-3 represents 2.5 * 10^-3, which is equal to 0.0025.
# Floats can be created using decimal notation, e.g., 10.5, or using scientific notation, e.g., 1.5e2.
# Floats can also be negative, e.g., -5.5.
# Floats can be used in mathematical operations just like integers, including addition, subtraction, multiplication, and division.
# Python also supports float division, which returns a float result even if the division is exact.
x = 10.5
y = -5.5
z = 1.5e2
w = 2.5e-3

print(type(x)) # <class 'float'>
print(type(y)) # <class 'float'>
print(type(z)) # <class 'float'>
print(type(w)) # <class 'float'>

#complex
# A complex number is a number that has both a real and an imaginary part.
# Complex numbers are represented in Python using the complex data type, which is a built-in type for representing complex numbers.
# Complex numbers can be created using the complex() function or by using the j suffix to indicate the imaginary part.
# For example, 3 + 4j represents a complex number with a real part of 3 and an imaginary part of 4.
# Similarly, 5 - 2j represents a complex number with a real part of 5 and an imaginary part of -2.
# Complex numbers can be used in mathematical operations just like integers and floats, including addition, subtraction, multiplication, and division.
# Python also supports complex conjugation, which is the operation of changing the sign of the imaginary part of a complex number.
# The complex conjugate of a complex number a + bj is a - bj.
# The complex() function can be used to create complex numbers from real and imaginary parts.
# The real and imaginary parts of a complex number can be accessed using the real and imag attributes, respectively.
# The abs() function can be used to get the magnitude (absolute value) of a complex number.
# The phase() function can be used to get the phase angle (argument) of a complex number.
x = 3 + 4j
y = 5 - 2j
z = complex(3, 4)
w = complex(5, -2)
print(type(x)) # <class 'complex'>
print(type(y)) # <class 'complex'>  
print(type(z)) # <class 'complex'>
print(type(w)) # <class 'complex'>

#type conversion
# Type conversion is the process of converting a value from one data type to another.
# In Python, you can convert between different data types using built-in functions. The most common type conversion functions are:
# 1. int(): Converts a value to an integer.
# 2. float(): Converts a value to a float.
# 3. str(): Converts a value to a string.
# 4. bool(): Converts a value to a boolean.
# 5. list(): Converts a value to a list.
# 6. tuple(): Converts a value to a tuple.
# 7. set(): Converts a value to a set.  
# 8. dict(): Converts a value to a dictionary.
# 9. complex(): Converts a value to a complex number.
# 10. bytes(): Converts a value to bytes.
# 11. bytearray(): Converts a value to a bytearray.
# 12. memoryview(): Converts a value to a memoryview.
# 13. frozenset(): Converts a value to a frozenset.
# 14. range(): Converts a value to a range object.
# 15. NoneType: Represents the absence of a value or a null value.
# 16. Enum: Represents a set of named values.
x = 5
y = 2.5
z = "10"
w = True
v = [1, 2, 3]
u = (1, 2, 3)
t = {1, 2, 3}
s = {"name": "John", "age": 36}
a = 3 + 4j
b = b"Hello"
c = bytearray(5)
d = memoryview(bytes(5))
e = frozenset({"apple", "banana", "cherry"})
f = range(5)
g = None
h = 5.0

a = float(x) # Converts x to an float
b = int(y) # Converts y to an int
c = int(z) # Converts z to a int
d = str(x) # Converts x to a string

print(type(a)) # <class 'float'>
print(type(b)) # <class 'int'>
print(type(c)) # <class 'int'>  
print(type(d)) # <class 'str'>

print(type(e)) # <class 'frozenset'>
print(type(f)) # <class 'range'>    
print(type(g)) # <class 'NoneType'>
print(type(h)) # <class 'float'>


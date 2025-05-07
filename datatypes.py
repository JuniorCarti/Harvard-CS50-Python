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

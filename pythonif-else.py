#Python Conditions and If statements
#Python supports the usual logical conditions from mathematics:
#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b

a=33
b=45

if a < b:
    print("a is less than b")

#Elif
#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
a=33
b=45

if a < b:
    print("a is less than b")
elif a >= b:
    print("b is greater than a")

#else keyword
#The else keyword catches anything which isn't caught by the preceding conditions.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
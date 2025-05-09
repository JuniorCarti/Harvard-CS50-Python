#Slicing
#Slicing is a way to extract a portion of a string
#You can use the slice() method to slice a string
#The slice() method takes three arguments: start, stop, and step
#The start argument is the index of the first character to include in the slice
#The stop argument is the index of the first character to exclude from the slice
#The step argument is the number of characters to skip between each character in the slice
#The slice() method returns a new string that contains the characters in the specified range
#You can also use the slice operator (:) to slice a string
#The slice operator takes two arguments: start and stop
#The start argument is the index of the first character to include in the slice
#The stop argument is the index of the first character to exclude from the slice
#The slice operator returns a new string that contains the characters in the specified range
#The slice operator can also take a third argument: step
#The step argument is the number of characters to skip between each character in the slice
#The slice operator returns a new string that contains the characters in the specified range
#The slice operator can also take a negative index
#The negative index counts from the end of the string
#The negative index starts at -1 for the last character in the string
#The negative index starts at -2 for the second to last character in the string
#The negative index starts at -3 for the third to last character in the string
#The negative index starts at -4 for the fourth to last character in the string
#The negative index starts at -5 for the fifth to last character in the string
#The negative index starts at -6 for the sixth to last character in the string
#The negative index starts at -7 for the seventh to last character in the string
#The negative index starts at -8 for the eighth to last character in the string
#The negative index starts at -9 for the ninth to last character in the string
#The negative index starts at -10 for the tenth to last character in the string
#The negative index starts at -11 for the eleventh to last character in the string
#The negative index starts at -12 for the twelfth to last character in the string
#The negative index starts at -13 for the thirteenth to last character in the string
#The negative index starts at -14 for the fourteenth to last character in the string
#The negative index starts at -15 for the fifteenth to last character in the string

b = "Hello World"
c = "Hello World"
print(b[0:5])
print(c[0:5])

#Slice From the Start
#You can omit the start index and the slice will start at the beginning of the string
#x = "Hello World"
#y = "Hello World"
x = "Hello World"
y = "Hello World"
print(x[:5])
print(y[:5])

#Slice To the End
#You can omit the end index and the slice will go to the end of the string
#x = "Hello World"
#y = "Hello World"
x = "Hello World"
y = "Hello World"
print(x[5:])
print(y[5:])
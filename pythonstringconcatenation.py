#python string concatenation
# # Concatenation is the process of joining two or more strings together
# # You can use the + operator to concatenate strings
# # You can also use the join() method to concatenate strings
# # The join() method takes a list of strings as an argument and returns a single string
# # The join() method is more efficient than using the + operator for concatenating large numbers of strings
# # The join() method is also more readable than using the + operator
# # The join() method is also more flexible than using the + operator
# # The join() method can be used to concatenate strings with a separator
# # The join() method can be used to concatenate strings with a prefix and suffix
# # The join() method can be used to concatenate strings with a custom separator
# # The join() method can be used to concatenate strings with a custom prefix and suffix
# # The join() method can be used to concatenate strings with a custom separator and prefix and suffix
# # The join() method can be used to concatenate strings with a custom separator and prefix and suffix and a custom format
a = "Hello"
b = "World"
c = "!"
d = " "
e = " "
f = " "
g = " "
h = " "
i = " "
j = " "
k = " "
l = " "
m = " "
n = " "
o = " "
p = " "
q = " "
r = " "
s = " "
t = " "
u = " "
v = " "
w = " "
x = " "
y = " "
z = " "
print(a + b + c)
print(a + d + b + c)
print(a + e + b + c)
print(a + f + b + c)
print(a + g + b + c)
print(a + h + b + c)
print(a + i + b + c)


s = "Hello"
t = "World"
u = "!"
print(s + t + u)
joined_string = " ".join([s, t, u])
print(joined_string)

# Concatenating strings with a separator
separator = ", "
joined_string_with_separator = separator.join([s, t, u])
print(joined_string_with_separator)

# Concatenating strings with a prefix and suffix
prefix = "Greeting: "
suffix = "!"
joined_string_with_prefix_suffix = prefix + separator.join([s, t]) + suffix
print(joined_string_with_prefix_suffix)

# Concatenating strings with a custom format
custom_format = "{} - {} - {}"
formatted_string = custom_format.format(s, t, u)
print(formatted_string)
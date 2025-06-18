# 1. f-strings (Formatted String Literals) – Best & Fastest
name = "Ridge"
age = 25
print(f"My name is {name} and I am {age} years old.")


#str.format() Method
template = "Hello {}, your score is {}"
print(template.format("Ridge", 87))


# Percentage (%) Formatting – Older style
name = "Ridge"
score = 90.1234
print("Hello %s, your score is %.1f" % (name, score))

#A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
#RegEx can be used to check if a string contains the specified search pattern.
#Python has a built-in package called re, which can be used to work with Regular Expressions.
#Import the re module:
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

text = "My number is 0712345678"
match = re.search(r"07\d{8}", text)
print(match.group())  # Output: 0712345678


text = "Emails: test@example.com, hello@gmail.com"
emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
print(emails)  # ['test@example.com', 'hello@gmail.com']

password = "Test1234"
if re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', password):
    print("Valid")
else:
    print("Invalid")

m = re.search(r"(\d+)", "Order number: 456")
print(m.group(0))  # '456'
print(m.start())   # Start index
print(m.end())     # End index


pattern = re.compile(r"\b\w{5}\b")  # Words of 5 letters
results = pattern.findall("Hello world! These words have five chars.")
print(results)  # ['Hello', 'world', 'These']

text = "My email is test@example.com"
new_text = re.sub(r"\S+@\S+", "[hidden email]", text)
print(new_text)  # My email is [hidden email]

text = "HELLO\nhello"
matches = re.findall(r"^hello", text, re.IGNORECASE | re.MULTILINE)
print(matches)  # ['HELLO', 'hello']





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


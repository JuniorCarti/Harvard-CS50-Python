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


import re

number = "0712345678"
pattern = r"^07\d{8}$"

if re.match(pattern, number):
    print("Valid Kenyan number")
else:
    print("Invalid")

import re

text = "Contact us at help@company.com or support@service.co.ke"
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print(emails)


password = "StrongP@ss1"
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"

if re.match(pattern, password):
    print("Strong password")
else:
    print("Weak password")

tweet = "Loving the #sunset at #LakeNaivasha! #KenyaVibes"
hashtags = re.findall(r"#\w+", tweet)
print(hashtags)


id_number = "12345678"
if re.match(r"^\d{8,}$", id_number):
    print("Valid ID number")
else:
    print("Invalid ID")


text = "This product is shit and useless"
censored = re.sub(r"\bshit\b", "****", text, flags=re.IGNORECASE)
print(censored)






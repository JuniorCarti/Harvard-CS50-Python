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

text = "Important dates: 01/06/2024, 17/06/2025."
dates = re.findall(r"\b\d{2}/\d{2}/\d{4}\b", text)
print(dates)


sentence = "Hey! How are you? I’m fine."
words = re.findall(r"\b\w+\b", sentence)
print(words)

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
match = re.search(r"v=([\w-]+)", url)
if match:
    print("Video ID:", match.group(1))

emails = ["user@outlook.com", "test@company.co.ke"]
domains = [re.search(r"@(.+)", email).group(1) for email in emails]
print(domains)

import re

plate = "KBX 321B"
pattern = r"^[Kk][A-Z]{2} \d{3}[A-Z]$"

if re.match(pattern, plate):
    print("Valid plate")
else:
    print("Invalid")


text = "Visit https://openai.com or http://google.com for info."
urls = re.findall(r"https?://[^\s]+", text)
print(urls)

sentence = "Ridge and Faith live in Nairobi but visit Eldoret often."
names = re.findall(r"\b[A-Z][a-z]+\b", sentence)
print(names)


amounts = ["KES 1,200", "KES 2500", "Ksh 340.75"]
cleaned = [re.sub(r"[^\d.]", "", amt) for amt in amounts]
print(cleaned)

time = "23:45"
if re.match(r"^(2[0-3]|[01]?[0-9]):[0-5][0-9]$", time):
    print("Valid time")


text = "This is is a test test of repeated repeated words words."
repeats = re.findall(r"\b(\w+)\s+\1\b", text)
print(repeats)

html = "<p>This is a <strong>paragraph</strong></p>"
tags = re.findall(r"</?[\w]+[^>]*>", html)
print(tags)

numbers = ["+254712345678", "+12025550123", "+442071838750"]
codes = re.findall(r"\+\d{1,4}", " ".join(numbers))
print(codes)

text = "Follow us @openai and @sprntAce on Twitter!"
handles = re.findall(r"@\w+", text)
print(handles)

text = "Ref No: AB123456C"
digits = re.findall(r"\d+", text)
print("".join(digits))  # Output: 123456

ip = "Server running at 192.168.1.1"
found = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", ip)
print(found)

text = "Programming in Python is amazing"
long_words = re.findall(r"\b\w{6,}\b", text)
print(long_words)

url = "https://www.example.com/page"
pattern = r"^https?://(www\.)?[\w\-]+\.\w+(/\S*)?$"

if re.match(pattern, url):
    print("Valid URL")

postal_code = "30100"
if re.match(r"^\d{5}$", postal_code):
    print("Valid postal code")
    
text = "The invoice 348 was paid on 2025-06-17, with 2 items."
numbers = re.findall(r"\d+", text)
print(numbers)  # ['348', '2025', '06', '17', '2']


name = "FaithWanjiru"
if re.match(r"^[A-Za-z]+$", name):
    print("Valid name")


email = "user1234@gmail.com"
masked = re.sub(r"(?<=.).(?=[^@]*?@)", "*", email)
print(masked)  # u*******@gmail.com

text = "Pay KES 1200 or Ksh 150.75 by Friday."
prices = re.findall(r"(?:KES|Ksh)\s?\d+(?:\.\d+)?", text)
print(prices)


username = "ridge_jnr_99"
if re.match(r"^[a-zA-Z0-9_]{3,15}$", username):
    print("Valid username")

code = "first_name = 'Faith'; last_name = 'Kiprono';"
snake_case = re.findall(r"\b[a-z]+(?:_[a-z]+)+\b", code)
print(snake_case)

ip6 = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
if re.match(r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$", ip6):
    print("Valid IPv6")

text = "UNICEF and NASA are well-known organizations"
acronyms = re.findall(r"\b[A-Z]{2,}\b", text)
print(acronyms)  # ['UNICEF', 'NASA']

text = "The values were 3.14, 2.71 and 100.0"
decimals = re.findall(r"\b\d+\.\d+\b", text)
print(decimals)


#Extract Kenyan ID and Passport Format
# National ID (8 digits) or Passport (2 letters + 7 digits)
ids = "ID: 12345678, Passport: CK1234567"
matches = re.findall(r"\b(?:\d{8}|[A-Z]{2}\d{7})\b", ids)
print(matches)


#Extract Kenyan MPESA Transaction Codes
text = "Transaction: QJD23KJ92 confirmed for Ksh 500"
mpesa_code = re.findall(r"\b[A-Z0-9]{10}\b", text)
print(mpesa_code)





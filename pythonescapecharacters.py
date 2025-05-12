#Escape Character
#Escape characters are characters that have a special meaning in Python strings.
#Escape characters are used to represent characters that cannot be typed directly into a string.
#Escape characters are often used to represent special characters such as newlines, tabs, and quotes.
#Escape characters are also used to represent characters that have a special meaning in Python strings, such as backslashes and quotes.
#Escape characters are often used in string formatting to create dynamic strings.
#You will get an error if you use double quotes inside a string that is surrounded by double quotes:

#txt = "We are the so-called "Vikings" from the north."
#You will get an error if you use single quotes inside a string that is surrounded by single quotes:
#txt = 'We are the so-called 'Vikings' from the north.'
#You will get an error if you use backslashes inside a string that is surrounded by backslashes:
#txt = "We are the so-called \Vikings\ from the north."
#You will get an error if you use newlines inside a string that is surrounded by newlines:
#txt = "We are the so-called
#Vikings
#from the north."
#You will get an error if you use tabs inside a string that is surrounded by tabs:
##   Vikings
  #  from the north."
#You will get an error if you use quotes inside a string that is surrounded by quotes:
#txt = "We are the so-called "Vikings" from the north."
#You will get an error if you use quotes inside a string that is surrounded by quotes:
#to solve this problem, you can use escape characters.
#Escape characters are characters that have a special meaning in Python strings.
#Escape characters are used to represent characters that cannot be typed directly into a string.
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#txt = 'We are the so-called \'Vikings\' from the north.'
# print(txt)
# txt = "We are the so-called \Vikings\ from the north."
# print(txt)
txt = "We are the so-called \nVikings\nfrom the north."
print(txt)

txt = "We are the so-called \tVikings\tfrom the north."
print(txt)
txt = "We are the so-called \bVikings\bfrom the north."
print(txt)
#meaning of \b is backspace
txt = "We are the so-called \rVikings\rfrom the north."
print(txt)
#meaning of \r is carriage return
txt = "We are the so-called \aVikings\afrom the north."
print(txt)
#meaning of \a is alert
txt = "We are the so-called \fVikings\ffrom the north."
print(txt)


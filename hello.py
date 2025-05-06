#print("What's your name?")
#input("What's your name? ")
#print("Hello, Ridge")

#return values
#variables - container for some value
#Ask user for their name
name = input("What's your name? ").strip().title() # clean code now

# Split users name into first name and last name
first, last = name.split(" ")
#Say hello to user
#print("hello," + name) concatenation
#multiple arguments
#print("hello,", name)
#print("hello, ", end="")
#print(name)
#positional paramaters,
#named parameters sep, end

#name = name.strip() #remove whitespace from str
#name = name.capitalize() # capitalize users name
#name = name.title() #capitalize each letter of the word

#name = name.strip().title # remove whitespace from str and capitalize each letter of the name

#print(f"hello, {name} ") #special string format str

print(f"hello, {first} ") #split



#print("hello, world")



#functions
#arguments-input to a function that influences its behaviour
#side effects 
#bugs are problems you face
#pseudocode - only comments no code, structuring your to-do list
#docs python.org
#the print function
#print(*objects, sep='' , end='\n' , file=sys.stdout, flush=False)
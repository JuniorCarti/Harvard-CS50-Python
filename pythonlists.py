#python lists
# #python lists are used to store multiple values in a single variable.
mylist = ["apple", "banana", "cherry"]
print(mylist)

#Lists are created using square brackets:
thislist = ["apple", "banana", "cherry"]
print(thislist)

#Lists are ordered, changeable, and allow duplicate values.
#Lists are ordered, meaning that the items have a defined order, and that order will not change.
#When you create a list, you will always get the same order.
#If you add new items to a list, the new items will be placed at the end of the list.
#list length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#List items are indexed, the first item has index [0], the second item has index [1], etc.
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
print(thislist[0])
print(thislist[2])
print(thislist[-1])
print(thislist[-2])
print(thislist[-3])

#List items can be of any data type:
thislist = ["apple", "banana", "cherry", 1, 2, 3]
print(thislist)


#type of list
thislist = ["apple", "banana", "cherry"]
print(type(thislist))

#the list constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#Python - Access List Items
#You can access the list items by referring to the index number:
thislist = ["apple", "banana", "cherry"]
print(thislist[0]) #first item
print(thislist[1]) #second item
print(thislist[2]) #third item
print(thislist[-1]) #last item
print(thislist[-2]) #second last item
print(thislist[-3]) #third last item

#range of indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(thislist[2:5]) #items from index 2 to index 5 (not included)
print(thislist[:4]) #items from index 0 to index 4 (not included)
print(thislist[2:]) #items from index 2 to the end
print(thislist[-4:-1]) #items from index -4 to index -1 (not included)
print(thislist[-4:]) #items from index -4 to the end
print(thislist[:-1]) #items from index 0 to index -1 (not included)
print(thislist[-1:]) #items from index -1 to the end
print(thislist[1:4]) #items from index 1 to index 4 (not included)

#Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
if "banana" in thislist:
    print("Yes, 'banana' is in the fruits list")
if "cherry" in thislist:
    print("Yes, 'cherry' is in the fruits list")
if "orange" in thislist:
    print("Yes, 'orange' is in the fruits list")
if "kiwi" in thislist:
    print("Yes, 'kiwi' is in the fruits list")

    #python - Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
thislist[0] = "watermelon"
print(thislist)
thislist[2] = "kiwi"
print(thislist)

#change a range of item values
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon", "kiwi", "mango"] 
print(thislist)

#Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["blackcurrant"]
print(thislist)

#Change the second and third value by replacing it with two values:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#The insert() method inserts an item at the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
thislist.insert(2, "kiwi")
print(thislist)
thislist.insert(3, "mango")
print(thislist)
thislist.insert(4, "watermelon")
print(thislist)
thislist.insert(5, "blackcurrant")
print(thislist)

mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist[1])

#Python - Add List Items
#append() method
#The append() method adds an item to the end of the list:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
thislist.append("kiwi")
print(thislist)
thislist.append("mango")
print(thislist)

#extend() method
#The extend() method adds the elements of an iterable (list, set, tuple, etc.) to the end of the current list:
thislist = ["apple", "banana", "cherry"]
thislist.extend(["orange", "kiwi", "mango"])
print(thislist)
thislist.extend(["watermelon", "blackcurrant"])

#Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thislist.extend(("orange", "kiwi", "mango")) # note the double round-brackets
print(thislist)
thislist.extend({"watermelon", "blackcurrant"})
print(thislist)

#remove() method
#The remove() method removes the specified item:
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#remove the specified index
thislist = ["apple", "banana", "cherry"]
thislist.remove(thislist[1])
print(thislist)

#remove the specified item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")   
print(thislist)
thislist.remove("cherry")
print(thislist)
thislist.remove("apple")
print(thislist)

#remove the first occurrence of the specified value
thislist = ["apple", "banana", "cherry", "banana"]
thislist.remove("banana")
print(thislist)


#pop() method
#The pop() method removes the specified index, (or the last item if index is not specified):
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#pop the last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#pop the first item
thislist = ["apple", "banana", "cherry"]
thislist.pop(0)
print(thislist)

#del keyword
#The del keyword removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[1]
print(thislist)
#del the last item
thislist = ["apple", "banana", "cherry"]
del thislist[-1]
print(thislist)

#del the whole list
thislist = ["apple", "banana", "cherry"]
#del thislist #this will cause an error because "thislist" no longer exists
print(thislist)
#The clear() method empties the list:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


#python loop lists
#You can loop through the list items by using a for loop:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

#You can also use a while loop to loop through the list items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1
#You can also loop through the list items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])
#You can also loop through the list items by using a while loop:
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1
#Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
newlist = [x for x in thislist]
print(newlist)
#Looping Using List Comprehension with Condition
thislist = ["apple", "banana", "cherry"]
newlist = [x for x in thislist if "a" in x]
print(newlist)

#list comprehension
thislist = ["apple", "banana", "cherry"]
newlist = []
for x in thislist:
    newlist.append(x)
print(newlist)

#List Comprehension
#List comprehension is a concise way to create lists.
#It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
#The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.
#For example, to create a list of squares:
thislist = [x**2 for x in range(10)]
print(thislist)
#List Comprehension with Condition
#You can also add conditions to the list comprehension, to create a list of squares, but only for even numbers:
thislist = [x**2 for x in range(10) if x % 2 == 0]
print(thislist)
#List Comprehension with Multiple For Clauses
#You can also use multiple for clauses in a list comprehension:
thislist = [x + y for x in ["apple", "banana", "cherry"] for y in ["orange", "kiwi", "mango"]]
print(thislist)

#List Comprehension with Nested Loops
thislist = [x + y for x in ["apple", "banana", "cherry"] for y in ["orange", "kiwi", "mango"]]
print(thislist)
#List Comprehension with Nested Loops
thislist = [x + y for x in ["apple", "banana", "cherry"] for y in ["orange", "kiwi", "mango"]]
print(thislist)

#the syntax of list comprehension
#newlist = [expression for item in iterable if condition == True]
#The expression is the current item in the iteration, but it is also the outcome, or result, of the iteration.
#The for item in iterable is a for loop that goes through the iterable, collecting the items.
#The if condition is like a filter that only accepts the items that evaluate to True.
#The result is a new list, leaving the old list unchanged.
#The filter() function
#The filter() function is used to create an output list of values that pass a certain condition from a function.
#The filter() function takes two arguments: a function and an iterable.
#The function is a test that is run for each item in the iterable. The items that evaluate to True are included in the result.
#The filter() function returns an iterator, so you need to convert it to a list to see the result.
#The filter() function can be used to filter a list of numbers:
thislist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def myfunc(x):
    if x % 2 == 0:
        return True
    else:
        return False
thislist = list(filter(myfunc, thislist))
print(thislist)

#The filter() function can be used to filter a list of strings:
thislist = ["apple", "banana", "cherry", "kiwi", "mango"]
def myfunc(x):
    if "a" in x:
        return True
    else:
        return False
thislist = list(filter(myfunc, thislist))
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist[0] = "watermelon"
print(thislist)

#python - Sort Lists
#The sort() method sorts the list ascending by default.
thislist = ["banana", "cherry", "apple"]
thislist.sort()
print(thislist)

#Sort Descending
thislist = ["banana", "cherry", "apple"]
thislist.sort(reverse = True)
print(thislist)

#Sort the list numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Sort the list numerically in descending order
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Sort the list alphabetically
thislist = ["banana", "cherry", "apple"]
thislist.sort()
print(thislist)

#custom sort function
thislist = ["BANANA", "cherry", "apple"]
thislist.sort(key = str.lower)
print(thislist)

#Sort the list based on how close the number is to 50:
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = lambda x: abs(x - 50))
print(thislist)

#Sort the list based on how close the number is to 50, descending:
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = lambda x: abs(x - 50), reverse = True)
print(thislist)
#Sort the list based on how close the number is to 50, ascending:
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = lambda x: abs(x - 50), reverse = False)
print(thislist)

#Case Insensitive Sort
thislist = ["banana", "Cherry", "apple"]
thislist.sort(key = str.lower)
print(thislist)

#Sort the list based on the length of the values
thislist = ["banana", "cherry", "apple"]
thislist.sort(key = len)
print(thislist)
#Sort the list based on the length of the values, descending
thislist = ["banana", "cherry", "apple"]
thislist.sort(key = len, reverse = True)
print(thislist)

#Sort the list based on the length of the values, ascending
thislist = ["banana", "cherry", "apple"]
thislist.sort(key = len, reverse = False)
print(thislist)
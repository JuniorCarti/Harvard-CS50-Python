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
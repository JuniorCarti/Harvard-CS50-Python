#python iterators
#An iterator is an object that contains a countable number of values.
#An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
#Technically, in Python, an iterator is an object which implements the iterator protocol, 
#which consist of the methods __iter__() and __next__().
#Iterator vs Iterable
#Lists, tuples, dictionaries, and sets are all iterable objects. 
# They are iterable containers which you can get an iterator from.
#All these objects have a iter() method which is used to get an iterator:

trucks = ("Volvo", "Scania", "ManTGX", "DAF", "Mercede-Benz")
my_iter = iter(trucks)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

#__iter__() - Returns the iterator object itself
#__next__() - Returns the next item from the collection
#How Iterators Work
#When you use a for loop in Python, it automatically creates 
#an iterator object and calls the next() method on each iteration until it catches the StopIteration exception.
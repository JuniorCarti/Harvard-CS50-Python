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

my_list = [1, 2, 3, 4]
my_iter = iter(my_list)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


#Creating Custom Iterators
#You can create your own iterator by implementing the __iter__() and __next__() methods in a class.
class CountDown:
    def __init__(self, start):
        self.current = start
        self.start = start
    
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            num = self.current
            self.current -= 1
            return num

counter = CountDown(5)
for num in counter:
    print(num)

#Database query
# Pseudocode example
class DatabaseIterator:
    def __init__(self, query):
        self.query = query
        self.position = 0
    
    def __next__(self):
        if self.position >= len(self.query.results):
            raise StopIteration
        record = self.query.results[self.position]
        self.position += 1
        return record
    
#reading large files
def process(line):
    # Example processing: print the line
    print(line.strip())

with open('huge_file.txt') as f:
    for line in f:  # file objects are iterators
        process(line)
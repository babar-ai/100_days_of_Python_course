#enumerate() function
'''

The enumerate() function in Python is a built-in utility used to iterate over an iterable (like a list, tuple, or string) while keeping track 
of both the index and the value of each item.
Syntax
enumerate(iterable, start=0)

How It Works
The enumerate() function returns an enumerator object, which generates pairs of index and value for each item in the iterable during iteration. 
You can use it directly in a for loop or convert it to a list or other collection
'''

#example 
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

#OR

fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits, start=1):
    print(f"Index: {index}, Fruit: {fruit}")

#Converting enumerate to a List

fruits = ['apple', 'banana', 'cherry']
index = list(enumerate(fruits))
print(index)


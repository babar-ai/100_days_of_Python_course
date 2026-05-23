
name = "babar"
print(name.upper())

# rstrip() method 
"""
The rstrip() method in Python is a built-in string method that removes trailing characters (characters at the end) of a string.
By default, it removes any whitespace characters (spaces, tabs, newlines, etc.) from the right end of the string.

"""
greeting  = "hello i am good!!!!!!!"
result = greeting.strip('!')
print(result)


#replace()

a = "babar"
print(a.replace("babar","tayyab"))

#split()
'''
convert string into list
'''
name = "pakistan zindabad"
list = name.split()
print(list)                #output ['pakistan', 'zindabad']

#capitalize()
'''
convert the first character in string into capitalized latter
'''

health = "i am good"
print(health.capitalize())  #output : I am good


#count()
'''
The count() method in Python is used to count the number of
occurrences of a specified value (substring) in a string, list, or tuple. Its behavior depends on the data type.
'''
medican = "i eat parasetamol one is \"panadol\" & the second one is parasetamol tables aranak "
print(f"word parasetamol is repeated {medican.count('parasetamol')} times")


#find()
'''
The find() method in Python is used to search for a substring within a string. It returns the index of the first 
occurrence of the substring if found; otherwise, it returns -1.
'''
text = "hello world!"
print(text.find('world'))  #output 6

#index()
'''
similar to find() except it will aris exception if the specific world is not avaliable
'''
name = "Babar Raheem"
# print(name.index('khan'))   #output: ValueError: substring not found

#split() fun 
'''
The split() function in Python is a string method used to break a string into a list of substrings based on a specified delimiter. If no delimiter is specified, it defaults to whitespace (spaces, tabs, and newlines).

Syntax
string.split(separator, maxsplit)

'''
#example

string = "i am ai develper"
list_str = string.split()
print(list_str)




#join()
'''
The join() function in Python is used to concatenate elements of a list (or any iterable) into a single string, with a specified separator between each element.


string.join(iterable)

'''
#example 

L = ['hello', 'ali']
my_str = ' '.join(L)
print(my_str)
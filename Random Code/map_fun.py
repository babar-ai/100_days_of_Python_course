 
'''
What is map()?
The map() function allows you to apply a function to each item in an iterable (like a list, tuple, or string) 
and returns a map object (which can be converted into a list, tuple, etc.).

It’s very useful when you want to transform or process all elements in a collection without writing a loop.

 syntax
 map(funtion, iterable (ie list, tuple))
 
function → a function that will be applied to each item (can be a normal function or a lambda function)
iterable → the sequence you want to process (like a list, tuple, or set)

'''

 
def make_even(num):
    
    if num % 2 == 1:
        return num+1
    else:
        return num
    

x = [441, 553, 445, 665]

#now we have two option 
#option 1 
even_num = []
for i in x:
    even_num.append(make_even(i))

print(f'using loop \n {even_num}')

# 2nd Optimistic Aproch

even_num = list(map(make_even, x))
print(f'using map fun \n {even_num}')


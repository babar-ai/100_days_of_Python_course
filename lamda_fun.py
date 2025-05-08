# lamda_funtion
'''
A lambda function in Python is an anonymous (nameless) function that is defined using the "lambda" keyword.
It can have any number of input arguments but only a single expression.
Lambda functions are typically used for short, simple operations where defining a full def function would be unnecessary.

syntax:
lambda arguments: expression

'''

add = lambda x, y: x+y

print(add(2,3))

# Lambda with filter()

numbers = [2,3,4,2,5,3,6]
even_no = filter(lambda x: x%2==0, numbers)
print(list(even_no)) 
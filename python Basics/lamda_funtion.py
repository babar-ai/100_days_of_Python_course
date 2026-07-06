'''
Lambda function in Python is a small anonymous function.

Anonymous means no funtion name 

#syntex

lambda parameters: return_value

note: here parameter referes to arguments (input to a funtion)

## Why Use Lambda?

Because sometimes writing full function is unnecessary.

Limitation of Lambda

Lambda can contain only one expression

i.e 
not allowed 
lambda x:
    a = x+1
    return a

Example:

'''

cal_percentage = lambda *marks: (
    sum(marks) / (len(marks)* 100)
)

print(cal_percentage(80, 70, 75, 88, 90))


# anther way:

percentage = lambda eng, math, phy, chem: (
    (eng + math + phy + chem) / 400
) * 100

print(percentage(80, 90, 75, 85))




#example 2

numbers = [1,2,3,4,5,6]

# to keep only even number 

is_even = lambda x: x % 2 == 0

result = [
    x
    for x in numbers
    if is_even(x)
]

print(result)
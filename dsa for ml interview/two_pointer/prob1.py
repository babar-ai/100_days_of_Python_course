
'''
problem :

You're tasked with figuring out the pair of elements where arr[p] + arr[q] add up to a certain number. (To try this problem out, check the Two Sum and Sorted Two Sum problems here.)

The brute force solution is to compare each element with every other number, but that's a time complexity of O(n²). We can do better!

'''

arr = [1, 2, 3, 4, 5]

#task : return two number whose sum is equal to 6

def find(arr: list):
    
    for i in range(len(arr)):

        for j in range(len(arr)):

            if i != j and arr[i] + arr[j] == 6:

                return i, j


values = find(arr)
print(values)
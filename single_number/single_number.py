'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

#Removed my previous solution and notes, found this solution from a video... The example from today's lecture is more realistic 
def single_number(arr):
    # Your code here
    integer = 0
    for i in arr: 
        integer ^= i
    return integer
    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

"""
for i in range(len(arr)):
# input: array of numbers where there is one number that 
# is not a duplicate; every other number has a duplicate 
# O(n^2)
#def single_number(arr):
#    for num in arr: # O(n)
#        if arr.count(num) == 1: # O(n)
#            return num
#
​
# O(n)
def single_number(arr):
    # sets are a closely-related cousin to dicts 
    # they don't associate values with keys 
    # they're useful for when you need the uniqueness
    # property of dicts
    s = set()
    # s = []
​
    for num in arr: # O(n)
        if num in s: # O(1)
            s.remove(num) # O(1)
        else:
            s.add(num) # O(1)
​
    # at this point, the only element in the set 
    # is our odd-element-out
#    return list(s)[0] # O(1)



"""
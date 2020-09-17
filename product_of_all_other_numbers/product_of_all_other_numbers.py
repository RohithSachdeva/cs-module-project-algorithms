'''
Input: a List of integers
Returns: a List of integers
'''
#Can think of a nested solution so not very efficient... 

def product_of_all_other_numbers(arr):
    #We will need to check two different iterating variables against each other. 
    #Set variable for array length, a new array, and a counter.  
    arr_length = len(arr)
    new_arr = [0] * arr_length
    counter = 0

    for i in range(len(arr)):
        item = 1
        for j in range(len(arr)): #Except when i and j are both at the same location in the array.. have item multiplied against position j 
            if j != i:
                item = item * arr[j]

        new_arr[counter] = item  #Add to the counter as you go through the array
        counter += 1

    return new_arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    #arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")


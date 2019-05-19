'''This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of
the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?'''


#Consideration 1: Do the elements in the array always increase at n+1?


def product_not_i(l=[]):
    ''' This function takes a list as an argument, and returns the produt of the list excluding the index element.'''
    new_list = []
    product = 1
    for element in l:
        product *= element
    for i in range(0,len(l)):
        p = product // l[i]
        new_list.append(p)
    return new_list

# Solution without Division
def product_not_i_wo_division(l=[]):
    ''' This function takes a list as an argument, and returns the produt of the list excluding the index element.'''

    new_list = []

    #loop over each element in (l) and create a list excluding the elment at index (i)
    for i in range(0,len(l)):
        exclusive_list = l[i+1:] + l[:i]
        product = 1

        #loop over the exclusive list and multiply each element
        for element in exclusive_list:
            product *= element
        new_list.append(product)
    return new_list

'''This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?'''

#Date: 5/16/2019
#Level: Easy

#Consideration 1: Can the list contain Negative Values?
#Consideration 2: Is a number considered type int or float or exclusively one type?
#Consideration 3: Can we use pre-compiled sort algorithms, or would you like me to define a sort method?
#Consideration 4: Can their be duplicates?


def sum_two_nums_in_a_list(l=[], k=None):
    '''This function determines if 2 numbers within a list (l) aggregate to the parameter k.

    :param l: the list of nums
    :param k: the target sum value
    :return: Bool indicating if there exists a sum or not
    '''

    # Sort List
    bound = sorted(list(set(l)))

    #Use the fact that (k-v) is the value that will evaluate this to true
    for v in bound:
        if k-v in bound:
            return True
    return False

if __name__ == "__main__":

    list1 = [-17, 0, 4, 34, 45, 56, 3]
    list2 = [-32, 0, 4, 17, 45, 56, 3, 27, 42, 36]

    test1 = sum_two_nums_in_a_list(list1, -17)
    test2 = sum_two_nums_in_a_list(list2, -17)

    print(test1)
    print(test2)

# Leslie Bacajol
# 11/09/21
# Problem 4
# This function takes a list of numbers and returns a new list with unique elements of the first list
# Using List [1, 3, 3, 3, 6, 2, 3,5] with the append function


def uniquel(some_list):
    unique_list = []
    for num in some_list:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list


print(uniquel([1, 3, 3, 3, 6, 2, 3, 5, 500, 500]))

# Leslie Bacajol
# 11/09/21
# Problem 3
# This function multiplies all the numbers in a list that contains [5, 2, 7, -1]


def multiplylist(some_list):
    total = 1
    # iterate each number in the list
    for num in some_list:
        total = num * total
    return total

my_list = [5, 2, 7, -1]
print(" The total is:", multiplylist(my_list))




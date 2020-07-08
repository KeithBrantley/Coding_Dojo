# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie_size(someList):
    new_list = []
    for i in someList:
        if i > 0:
            new_list.append('big')
        else:
            new_list.append(i)
    return new_list

# print(biggie_size([-1, 3, 5, -5]))

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(someList):
    sum = 0
    for i in range(len(someList)):
        if someList[i] >= 1:
            sum += 1
    someList[-1] = sum
    return someList

# print(count_positives([-1,1,1,1]))


# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sum_total(someList):
    total = 0
    for i in range(len(someList)):
        total = total + someList[i]
    return total

# print(sum_total([6,3,-2]))


# Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5

def average(someList):
    total = 0
    for i in range(len(someList)):
        total = total + someList[i]
    return total / len(someList)

# print(average([1,2,3,4]))


# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length(someList):
    for i in range(len(someList)):
        if len(someList) == 0:
            return 0
        else:
            return len(someList)

# print(length([37,2,1,-9]))


# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def minimum_value(someList):
    min_val = 0
    if len(someList) == 0:
        return False
    for i in someList:
        if i < min_val:
            min_val = i
    return min_val

# print(minimum_value([37,2,1,-9]))
# print(minimum_value([]))


# Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def maximum_value(someList):
    max_val = 0
    if len(someList) == 0:
        return False
    for i in someList:
        if i > max_val:
            max_val = i
    return max_val

# print(maximum_value([37,2,1,-9]))
# print(maximum_value([]))


# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(someList):
    analyze = {
        'sumTotal' : sum_total(someList),
        'average' : average(someList),
        'minimum' : minimum_value(someList),
        'maximum' : maximum_value(someList),
        'length' : length(someList)
    }
    return analyze
# print(ultimate_analysis([37,2,1,-9]))

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(someList):
    someList = someList[::-1]
    return someList
    
print(reverse_list([37,2,1,-9]))
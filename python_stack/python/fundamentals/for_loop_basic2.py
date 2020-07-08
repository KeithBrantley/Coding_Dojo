# 1. Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

# list = [-1, 3, 5, -5]
# def biggie_size():
#     for i in range(len(list)):
#         if list[i] > 0:
#             list[i] = "big"
#     return list

# print(biggie_size())

# 2. Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
# NOT DONE
list = [1,6,-4,-2,-7,-2]
def count_positives(list):
    new_list = []
    for num in list:
        if num in list[i] < 0:
            new_list.append(num)
            print(new_list)
    
    
print(count_positives(list))
    
    # num = 0
    # new_list = []
    # for i in range(len(list)):
    #     print(len(list))
    #     if num in list < 0:
    #         new_list.append(list[i])
    #         # print(new_list)
    #     return len(new_list)
      

# print(count_positives())

# 3. Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

# list = [1,2,3,4]
# def sum_total(list):
#     total = 0
#     for i in list:
#         total += i
#     return total

# print(sum_total(list))


# 4. Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5

# nums = [1,2,3,4]

# def average(nums):
#     total = 0
#     for i in nums:
#         total += i / len(nums)
#     return total

# print(average(nums))


# 5. Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

# nums = [37,2,1,-9]
# def nums_length(nums):
#     length = len(nums)
#     return length

# print(nums_length(nums))


# 6. Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

# list=[37,2,1,-9]
# def minimum(list):
#     min_num = list[0]
#     for i in list:       
#         if i < min_num:
#             min_num = i
#     return min_num

# print(minimum(list))
 
# print(minimum([])) 


# 7. Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

# def minimum(list):
#     min_num = list[0]
#     for i in list:       
#         if i > min_num:
#             min_num = i   
#         # else:
#         #     min_num == 0
#         #     return False  
#     return min_num

 
# # print(minimum([])) 
# print(minimum([37,2,1,-9]) )


# 8. Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

# def ultimate_analysis():



# 9. Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

# def reverse_list():
#     for i in range( len(list))
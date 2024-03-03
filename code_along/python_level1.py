
# my_string = "a b cd"

# print(my_string.split())

# # x = "I want {} and {}".format('dog', 'cat')
# out = "I want {x} and {y}".format(x = 'dog', y = 'cat')

# print(out)

# x = 'dog'
# y = 'cat'

# out = f"I want {x} and {y} again."

# print(out)

# x = [1,2,3,4]
# out = []

# for el in x:
#     out.append(el**2)

# print(out)

# print('List comprehension: \n', [val**2 for val in x])


# def square_function(arg1):

    
#     """ This is a square function. """
#     if type(arg1) == str:
#         arg1 = arg1.split()

#     return [int(val)**2 for val in arg1]
    

#     # return out

# # print(square_function(21))

# input1 = input('Enter first integer input:')
# # print(type(input1), input1)
# print('square value of your input: ', square_function(input1))

# input2 = input('Enter second list input:')
# # print(type(input2), input2)
# print('square value of your input: ', square_function(input2))

# def return_function(arg1):
    
#     out = arg1

#     return out

# print(return_function(2))

# list1 = [range(10)]

# print()


# def even_num(val):
#     return val%2 == 0


# list1 = list(range(20))

# even_lambda_fn = lambda num: num%2 == 0

# # print(list1)
# print(list(filter(even_num, list1)))
# print(list(filter(even_lambda_fn, list1)))
# print(list(filter(lambda num: num%2 == 0, list1)))

# Problem 1:
# def arrayCheck(arr):
#     """
#     Provide the array to check 1,2,3 pattern.
#     """
#     # print(len(arr)-2)
#     for ele_index in range(len(arr)-2):
#         # print(ele_index)

#         if ((1 == arr[ele_index]) and (2 == arr[ele_index+1]) and (3 == arr[ele_index+2])):
#             out = True
#             break;
#         else:
#             out = False
        
#     return out


# print(arrayCheck([1,2,3]))
# print(arrayCheck([1, 1, 2, 3, 1]))
# print(arrayCheck([1, 1, 4, 3, 1, 1]))

# Problem 2:
# def alt_position_string(input_string):
#     "This fucntion return the string where values are taken from only alternate position."
    
#     out_string = ''
    
#     for idx, val in enumerate(input_string):
#         if idx%2 ==0 :
#             out_string = out_string + val  
    
#     return out_string


# # print(alt_position_string('Heleleo'))
# print(alt_position_string('Hello'))
# print(alt_position_string('Hi'))

# Problem 3:
# def teen_value(list1):
#     out_list = []

#     for val in list1:
#         if val in [13,14,17,18,19]:
#             out_list.append(0)
#         else:
#             out_list.append(val)

#     return out_list

# def no_teen_sum(list2):

#     out_list = teen_value(list2)
#     out = 0

#     for val in out_list:
#         out = out + val

#     return out

# print(no_teen_sum([1,2,3]))
# print(no_teen_sum([2,13,1]))
# print(no_teen_sum([2,1,14]))

# Difficult Problem
import numpy as np
import random

# np.random.seed(100)

digits = list(range(10))
random.shuffle(digits)

comp_number = ''.join([str(val) for val in digits[:3]])
# print(comp_number)

def match_result(comp_number, guessed_number):
    '''
    This function will return true if any of the input.
    '''

    digit_1 = guessed_number[0]
    digit_2 = guessed_number[1]
    digit_3 = guessed_number[2]
    
    out = 'nope'

    if (digit_1 in comp_number) or (digit_2 in comp_number) or (digit_3 in comp_number):
        out = 'close' # wrong position
    
    if (digit_1 in comp_number[0]) or (digit_2 in comp_number[1]) or (digit_3 in comp_number[2]):
        out = 'match'
    
    return out
    
not_a_match = True

print(comp_number)

while(not_a_match):
    user_input = input('What is your guess?')

    if user_input == comp_number:
        print('You have guessed the number correctly.')
        break;
    else:
        print(match_result(comp_number, user_input))
        continue











    












# Given an integer x perform the following conditional actions:
#
# If x is odd, return 'Red'
# If x is even and in the inclusive range of 2 to 5, return 'Blue'
# If x is even and in the inclusive range of 6 to 20, return 'Red'
# If x is even and greater than 20, return 'Blue'
#
# Constraint notes:
# an input integer is alway withing the range 1 to 100 inclusive
# """
def isEven(x):
    return x % 2 ==0


def isWithinRange (x, start, stop):
    return start < x < stop

def red_or_blue (x):
    if  not isEven(x) or (isWithinRange(x, 6, 20) and isEven(x)):
        return 'Red'

    if (isEven(x) or x > 20) or x in [2, 4]:
        return 'Blue'

print (red_or_blue(9))
# ### TASK TWO -- TDD ###
#
#
# """
# Let's write a test for our function first and then will write an actual code to ensure that
# all tests pass.
#
# Task
# Given a list of dictionaries where keys are student's  name and student's mark.
# calculate the average score for the exam.
#
# If mark is not within the range 1 to 10, raise an error
# Some mark values can be integers and some are strings, we need to process both
# If mark is missing, use value 5
#
# """
#
# ### TASK THREE -- MOCKING ###
#
# # review first to understand what's happening
# # write tests using mocking
#
# """
# read a file line by line and check the number of the last line.
# Extract that number, increment by 1 and return the new number
#
# If you have a file example.txt like this:
#
# 1. Melon
# 2. Pear
# 3. Apple
#
# Read the last line, extract number 3 and increment it by 1.
# """
#
#
# def get_file_content(file_name):
#     """
#     Read content of a file
#     :param file_name: str file name or path
#     :return: list of str where each str is a line
#
#     Example return:
#         [
#             '1. line',
#             '2. line',
#             '3. line',
#         ]
#     """
# #     with open(file_name, 'r') as file:
# #         return file.readlines()
# #
# #
# # def increment_line_number(file_name):
# #     content = get_file_content(file_name)
# #     num = int(content.pop().split('.')[0])
# #     return num + 1
#
#
#
#

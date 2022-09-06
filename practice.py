# print('--------------WELCOME TO MY CHOCOLATE STALL--------------\n')
# chocolates = {'white': 1.50, 'milk': 1.20, 'dark': 1.80, 'vegan': 2, }
# choice = str(input('Which chocolate would you like to purchase?'))
#
# if choice != (chocolates[choice]):
#     print(chocolates[choice])

import math

def centurify(year):
  century = int((year / 100) + 1)
  decade = math.floor(year%100/10)*10
  return f"{century}th century and {decade}s"

print(centurify(1981))



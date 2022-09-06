customer = input('Which chocolates would you like to buy?')

discount_applicable = discount_choice == 'y'

if discount_applicable:
     meal_price = meal_price * 0.9
     print('Discount applied')
else:
     print('No discount')

print('Total cost: {}'.format(meal_price))

# temperature = float(input('What is the temperature of the oven? '))
#
# if temperature > 200:
#     print('The oven is too hot')
# elif temperature < 150:
#     print('The oven is too cold')
# elif temperature == 180:
#     print('The oven is at the perfect temperature')
# else:
#     print('The temperature is close enough')
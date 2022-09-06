# English_Weather = input('Is it raining outside?')
# if English_Weather== 'y':
#     print("Take an umbrella")
# elif English_Weather == 'N':
#     print('You dont need an umbrella')
# else:
#     print('You dont need an umbrella')

# my_money = int(input('How much money do you have? '))
# boat_cost = 20 + 5
#
# if my_money >= boat_cost:
#     print('You can afford the boat hire')
# else:
#     print('You cannot afford the board hire')


# shopping_list = [
#     "oranges",
#     "cat food",
#     "sponge cake",
#     "long-grain rice",
#     "cheese board",
# ]
# print(shopping_list[0])

import random
def Lottery_Ticket():
    Lottery_Ticket = (2, 5, 12, 32, 84, 39, 78)

    random_number = random.randint(1, 7)

    print(random_number)

    if random_number != 1:
        side = 'tails'
    else:
        side = 'heads'
    return side

result = Lottery_Ticket()

print('You have won {}'.format(result))


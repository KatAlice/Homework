import random

ticket = [2, 12, 17, 25, 32, 37, 41]
draw = random.sample(range(0, 48), 7)
result = set(draw) & set(ticket)
matches = len(result)

if matches == 3:
    print('prize won: £20, yay!')
elif matches == 4:
    print('prize won: £40, yay!')
elif matches == 5:
    print('prize won: £100, yay!')
elif matches == 6:
    print('prize won: £1000, yay!')
elif matches == 7:
    print('prize won: £100,0000, WOWZER!')
else:
    print('Sorry, maybe next time! Thanks for trying!')
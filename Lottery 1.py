import random


def lottery():
    lottery_ticket = [2, 5, 12, 32, 84, 39, 78]
    lottery_numbers = []
    for i in range(0, 7):
        n = random.randint(1, 100)
        lottery_numbers.append(n)
        print(lottery_numbers)

        count = sum(f in lottery_ticket for f in lottery_numbers)

        if count == 3:
            print('Prize won: £20')
        elif count == 4:
            print('Prize won: £40')
        elif count == 5:
            print('Prize won: £100')
        elif count == 6:
            print('Prize won: £10000')
        elif count == 7:
            print('Prize won: £10000000')
        else:
            print('No prizes won')

    lottery()

def check_pin():
    i = 0
    while i < 3:
        pin = input('Enter pin code please:')
        if pin == '1234':
            print("access granter")
            account_balance()
        else:
            i += 1
    print("Account blocked")


def account_balance():
    i = 100
    while True:
        withdraw = input("How much would you like to withdraw £")
        try:
            withdraw = int(withdraw)
        except ValueError:
            print(withdraw, 'is not a number, try again.')
            continue
        if withdraw > i:
            print("    ")
            print("You don't have enough in the bank.")
            quit()
        else:
            i = i - withdraw
            print("Balance now £", i)
            quit()


check_pin()



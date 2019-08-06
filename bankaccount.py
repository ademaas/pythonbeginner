def option_form():
    print('SELECT OPTION:')
    print('D: Deposit')
    print('W: Withdrawl')
    print('N: Net')

    option = input('OPTION: ')

    return option

def calculatevalue():
    net=0
    option = option_form()

    while True:
        if option=='D':
            value = int(input('Deposit amount: '))
            net = net+value
            option = option_form()

        if option=='W':
            value = int(input('Withdrawal amount: '))
            net = net-value
            option = option_form()

        if option=='N':
            print('Net amount in the book is: ',net)

            break

def main():
    calculatevalue()


if __name__=="__main__":
    main()

    
    
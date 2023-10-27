balance = 0

def check_balance():
    print('Total balance:', balance)

def deposite(amt):
    global balance
    balance = balance + amt
    print(amt, 'Rs. deposited')

def withdraw(amt):
    global balance
    balance = balance - amt
    print(amt, 'Rs. withdrawn')

while True:
    choice = int(input('\nEnter choice\n1.CHECK BALANCE\t2.DEPOSIT\n3.WITHDRAW CASH\t4.EXIT\n'))
    match choice:
        case 1:
            print('CHECK BALANCE')
            check_balance()
        case 2:
            print('DEPOSIT CASH')
            d_amt = int(input('Enter amount to deposit:  '))
            deposite(d_amt)

        case 3:
            print('WITHDRAW CASH')
            w_amt = int(input('Enter amount to withdraw:  '))
            if w_amt > balance:
                print('\nInsufficient funds.....')
            else:
                withdraw(w_amt)

        case 4:
            print('EXITING....')

        case _:
            print('INVALID CHOICE....')





            






















            

            

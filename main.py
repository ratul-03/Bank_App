# Bank App
def show_balance():
    print(f"You balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter a amount to deposit: "))
    if (amount < 0):
        print("Invalid amount")
        return 0
    else:
        return amount

def with_Draw():
    amount = float(input("Enter a amount ti withdraw: "))

    #Logic
    if (amount > balance):
        print("Insufficent amount")
        return 0
    elif (amount < 0):
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

balance = 0
is_True = True

while(is_True):
    print("********************************")
    print("Banking App")
    print("********************************")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("********************************")

    # Taking Choise Input
    choice = input("Enter your choise (1 - 4): ")

    # Condition logic
    if (choice == '1'):
        show_balance()
    elif (choice == '2'):
        balance += deposit()
    elif (choice == '3'):
        balance -= with_Draw()
    elif (choice == '4'):
        is_True = False
    else:
        print("That is not a valid choice")
print("Thanks, Have a nice day")
# 
# Darbības ar masīviem - https://www.w3schools.com/python/python_arrays.asp
# Datu tipi, mekle float - https://www.w3schools.com/python/python_datatypes.asp
# Pārbaudēm izmanto if...else - https://www.w3schools.com/python/python_conditions.asp
# Cipari https://www.w3schools.com/python/python_numbers.asp
# 

balance = 0

while True:
    print("Banking Options:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print("How much do you want to deposit?")
        deposit = int(input())
        balance += deposit
        print("Your balance now is = " + str(balance))
        pass
    elif choice == '2':
        print("How much do you want to withdraw?")
        withdraw = int(input())
        if balance < withdraw:
            print("Unfortunatley you can't withdraw money from your bank account, because you don't have enough money.")
            pass
        elif balance > withdraw:
            balance -= withdraw
            print("Withdraw = " + str(withdraw))
        print("Your balance is = " + str(balance))
        pass
    elif choice == '3':
        print("Your balance is = " + str(balance))
        pass
    elif choice == '4':
        print("Exiting the banking system. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

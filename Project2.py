#ATM MACHINE SIMULATOR
print("--------- ATM SIMULATION ---------")

# initial user data
account = {
    "pin": "1234",
    "balance": 500000
}

# function to check balance
def check_balance():
    print("Your current balance is:", account["balance"])

# function to withdraw money
def withdraw():
    amount = int(input("Enter amount to withdraw: "))
    if amount <= account["balance"]:
        account["balance"] -= amount
        print("Withdrawal successful!")
        print("Remaining Balance:", account["balance"])
    else:
        print("Insufficient balance!")

# function to deposit money
def deposit():
    amount = int(input("Enter amount to deposit: "))
    account["balance"] += amount
    print("Deposit successful!")
    print("Updated Balance:", account["balance"])

# login using PIN
pin = input("Enter your ATM PIN: ")

if pin != account["pin"]:
    print("Incorrect PIN! Access denied.")
else:
    print("Login successful!")

    while True:
        print("\n------ MENU ------")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            withdraw()

        elif choice == "3":
            deposit()

        elif choice == "4":
            print("Thank you for using the ATM!")
            break

        else:
            print("Invalid option! Try again.")

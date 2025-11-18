print("=========== MULTI UTILITY PYTHON APPLICATION ===========")

# -------------------- LOGIN SYSTEM -----------------------
def login():
    print("\n----- LOGIN PAGE -----")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "prayas" and password == "1234":
        print("Login Successful!")
        return True
    else:
        print("Login Failed! Wrong Credentials")
        return False


# -------------------- SIMPLE CALCULATOR ------------------
def calculator():
    print("\n----- CALCULATOR -----")
    a = float(input("Enter 1st number: "))
    b = float(input("Enter 2nd number: "))
    print("1.Add 2.Subtract 3.Multiply 4.Divide")
    ch = input("Enter choice: ")

    if ch == "1":
        print("Result =", a + b)
    elif ch == "2":
        print("Result =", a - b)
    elif ch == "3":
        print("Result =", a * b)
    elif ch == "4":
        if b != 0:
            print("Result =", a / b)
        else:
            print("Cannot divide by zero!")
    else:
        print("Invalid Option!")


# ---------------------- TO-DO LIST ------------------------
todo = []

def todo_app():
    while True:
        print("\n------ TO-DO APP ------")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Back")

        ch = input("Enter choice: ")

        if ch == "1":
            t = input("Enter new task: ")
            todo.append(t)
            print("Task Added!")

        elif ch == "2":
            print("Your Tasks:")
            for i in todo:
                print("-", i)

        elif ch == "3":
            rem = input("Enter task to remove: ")
            if rem in todo:
                todo.remove(rem)
                print("Task Removed!")
            else:
                print("Task not found!")

        elif ch == "4":
            break
        else:
            print("Invalid choice!")


# ------------------ LIBRARY MANAGEMENT ---------------------
library = []

def library_app():
    while True:
        print("\n------ LIBRARY MANAGER ------")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Back")

        ch = input("Enter choice: ")

        if ch == "1":
            book = {}
            book["ID"] = input("Book ID: ")
            book["Title"] = input("Book Title: ")
            book["Author"] = input("Author: ")
            book["Status"] = "Available"
            library.append(book)
            print("Book Added!")

        elif ch == "2":
            print("\nBooks in Library:")
            for b in library:
                print(b)

        elif ch == "3":
            bid = input("Enter Book ID to issue: ")
            for b in library:
                if b["ID"] == bid:
                    if b["Status"] == "Available":
                        b["Status"] = "Issued"
                        print("Book Issued!")
                    else:
                        print("Book Already Issued!")
                    break
            else:
                print("Book Not Found!")

        elif ch == "4":
            bid = input("Enter Book ID to return: ")
            for b in library:
                if b["ID"] == bid:
                    b["Status"] = "Available"
                    print("Book Returned!")
                    break
            else:
                print("Book Not Found!")

        elif ch == "5":
            break
        else:
            print("Invalid choice!")


# --------------------- GRADE CALCULATOR --------------------
def grade_calculator():
    print("\n------ STUDENT GRADE CALCULATOR ------")
    name = input("Enter Student Name: ")
    m1 = int(input("Physics: "))
    m2 = int(input("Chemistry: "))
    m3 = int(input("Math: "))

    total = m1 + m2 + m3
    average = total / 3

    print("Total =", total)
    print("Average =", average)

    if average >= 90:
        print("Grade = A+")
    elif average >= 80:
        print("Grade = A")
    elif average >= 70:
        print("Grade = B")
    else:
        print("Grade = C")


# --------------------- NOTES APP (FILE) ---------------------
def notes_app():
    print("\n------ NOTES APP ------")
    note = input("Write your note: ")

    with open("notes.txt", "a") as f:
        f.write(note + "\n")

    print("Note Saved in notes.txt!")


# --------------------- ATM SIMULATION -----------------------
def atm_app():
    balance = 10000
    print("\n------ ATM SIMULATOR ------")

    while True:
        print("1. Check Balance\n2. Withdraw\n3. Deposit\n4. Exit")
        ch = input("Enter option: ")

        if ch == "1":
            print("Current Balance =", balance)

        elif ch == "2":
            amt = int(input("Enter withdraw amount: "))
            if amt <= balance:
                balance -= amt
                print("Withdraw Successful!")
            else:
                print("Insufficient Balance!")

        elif ch == "3":
            amt = int(input("Enter deposit amount: "))
            balance += amt
            print("Deposit Successful!")

        elif ch == "4":
            break

        else:
            print("Invalid option!")


# --------------------- BANK ACCOUNT (OOP) -------------------
class BankAccount:
    def __init__(self, name, bal):
        self.name = name
        self.balance = bal

    def deposit(self, amt):
        self.balance += amt
        print("Deposited!")

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
            print("Withdrawn!")
        else:
            print("Insufficient Balance!")

    def show(self):
        print("Balance =", self.balance)


def bank_oop_app():
    acc = BankAccount("Prayas", 5000)

    while True:
        print("\n------ OOP BANK ACCOUNT ------")
        print("1.Deposit 2.Withdraw 3.Check Balance 4.Back")
        ch = input("Enter choice: ")

        if ch == "1":
            amt = int(input("Amount: "))
            acc.deposit(amt)

        elif ch == "2":
            amt = int(input("Amount: "))
            acc.withdraw(amt)

        elif ch == "3":
            acc.show()

        elif ch == "4":
            break
        else:
            print("Invalid!")


# --------------------- MAIN MENU ----------------------------
if login():
    while True:
        print("\n================== MAIN MENU ==================")
        print("1. Calculator")
        print("2. To-Do List")
        print("3. Library Manager")
        print("4. Grade Calculator")
        print("5. Notes App")
        print("6. ATM Simulator")
        print("7. Bank App (OOP)")
        print("8. Exit")

        choice = input("Choose Option: ")

        if choice == "1":
            calculator()
        elif choice == "2":
            todo_app()
        elif choice == "3":
            library_app()
        elif choice == "4":
            grade_calculator()
        elif choice == "5":
            notes_app()
        elif choice == "6":
            atm_app()
        elif choice == "7":
            bank_oop_app()
        elif choice == "8":
            print("Thank you! Exiting App...")
            break
        else:
            print("Invalid Input!")

class BankAccount:
    def __init__(self, name, account_number, account_type, balance=0):
        self.name = name
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"\nDeposited: {amount}\nCurrent Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("\nInsufficient balance!")
        else:
            self.balance -= amount
            print(f"\nWithdrew: {amount}\nCurrent Balance: {self.balance}")

    def display_details(self):
        print(f"\nName : {self.name}")
        print(f"Account Number : {self.account_number}")
        print(f"Account Type : {self.account_type}")
        print(f"Balance : {self.balance}")

# User Input
name = input("Enter your name : ")
account_number = int(input("Enter your account number : "))
account_type = input("Enter account type (Savings/Current) : ")
balance = float(input("Enter initial balance : "))

account = BankAccount(name, account_number, account_type, balance)

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Display Details\n4. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == 3:
        account.display_details()
    elif choice == 4:
        break
    else:
        print("Invalid choice!")

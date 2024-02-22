import os

class ATM:
    def __init__(self):
        self.balance = 0
        self.file_path = "accounts.txt"
        self.load_balance()

    def load_balance(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                self.balance = float(file.read())

    def save_balance(self):
        with open(self.file_path, 'w') as file:
            file.write(str(self.balance))

    def check_balance(self):
        print(f"Your balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        self.save_balance()
        print(f"Deposited ${amount:.2f} successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.save_balance()
            print(f"Withdrawn ${amount:.2f} successfully.")
        else:
            print("Insufficient funds.")

def main():
    atm = ATM()

    while True:
        print("\n===== ATM Menu =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: $"))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: $"))
            atm.withdraw(amount)
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

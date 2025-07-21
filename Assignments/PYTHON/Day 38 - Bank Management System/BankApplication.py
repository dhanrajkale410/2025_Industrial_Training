from abc import ABC, abstractmethod

# Abstract class
class Account(ABC):
    def __init__(self, account_number, name, balance):
        self.__account_number = account_number
        self.__name = name
        self.__balance = balance

    @property
    def account_number(self):
        return self.__account_number

    @property
    def name(self):
        return self.__name

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        self.__balance = amount

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass


# Concrete class
class SavingsAccount(Account):
    MIN_BALANCE = 500

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance - amount >= SavingsAccount.MIN_BALANCE:
                self.balance -= amount
                print(f"₹{amount} withdrawn successfully.")
            else:
                print(f"Cannot withdraw. Minimum balance of ₹{SavingsAccount.MIN_BALANCE} must be maintained.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance


# Bank class
class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_accounts()

    def create_account(self, name, balance):
        if balance < SavingsAccount.MIN_BALANCE:
            print(f"Opening balance must be at least ₹{SavingsAccount.MIN_BALANCE}.")
            return None

        account_number = len(self.accounts) + 1001
        account = SavingsAccount(account_number, name, balance)
        self.accounts[account_number] = account
        self.save_accounts()
        print(f"Account created successfully! Account No: {account_number}")
        return account

    def find_account(self, account_number):
        return self.accounts.get(account_number)

    def save_accounts(self):
        with open("accounts.txt", "w") as f:
            for acc in self.accounts.values():
                f.write(f"{acc.account_number},{acc.name},{acc.balance}\n")

    def load_accounts(self):
        try:
            with open("accounts.txt", "r") as f:
                for line in f:
                    acc_no, name, balance = line.strip().split(",")
                    acc = SavingsAccount(int(acc_no), name, float(balance))
                    self.accounts[int(acc_no)] = acc
        except FileNotFoundError:
            pass  # No accounts file yet


# Main menu
def main():
    bank = Bank()
    while True:
        print("\n--- Welcome to Python Bank ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transfer Money")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            try:
                balance = float(input("Enter opening balance: "))
                bank.create_account(name, balance)
            except ValueError:
                print("Invalid amount entered.")

        elif choice == "2":
            try:
                acc_no = int(input("Enter account number: "))
                amount = float(input("Enter deposit amount: "))
                acc = bank.find_account(acc_no)
                if acc:
                    acc.deposit(amount)
                    bank.save_accounts()
                else:
                    print("Account not found.")
            except ValueError:
                print("Invalid input.")

        elif choice == "3":
            try:
                acc_no = int(input("Enter account number: "))
                amount = float(input("Enter withdrawal amount: "))
                acc = bank.find_account(acc_no)
                if acc:
                    acc.withdraw(amount)
                    bank.save_accounts()
                else:
                    print("Account not found.")
            except ValueError:
                print("Invalid input.")

        elif choice == "4":
            try:
                acc_no = int(input("Enter account number: "))
                acc = bank.find_account(acc_no)
                if acc:
                    print(f"Available Balance: ₹{acc.get_balance()}")
                else:
                    print("Account not found.")
            except ValueError:
                print("Invalid input.")

        elif choice == "5":
            try:
                from_acc_no = int(input("Enter sender account number: "))
                to_acc_no = int(input("Enter receiver account number: "))
                amount = float(input("Enter amount to transfer: "))

                from_acc = bank.find_account(from_acc_no)
                to_acc = bank.find_account(to_acc_no)

                if from_acc and to_acc:
                    if from_acc.get_balance() - amount >= SavingsAccount.MIN_BALANCE:
                        from_acc.withdraw(amount)
                        to_acc.deposit(amount)
                        bank.save_accounts()
                        print("Transfer successful.")
                    else:
                        print("Insufficient balance for transfer.")
                else:
                    print("One or both accounts not found.")
            except ValueError:
                print("Invalid input.")

        elif choice == "6":
            print("Thank you for using Python Bank. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

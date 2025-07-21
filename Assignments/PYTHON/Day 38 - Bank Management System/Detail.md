Task: Bank Management System

Features to Implement:

1. Create Bank Accounts
2. Deposit & Withdraw Money
3. Check Balance
4. Transfer Money between Accounts
5. Account Information Saved in a File (accounts.txt)
6. Use OOP Concepts:

   * Class
   * Inheritance
   * Encapsulation (private attributes)
   * Abstraction (using abc module)

Structure:

 1. Account (Abstract Class)

* account_number, name, balance → Private attributes
* deposit(), withdraw(), get_balance() → Abstract methods

2. SavingsAccount(Account)

* Implements deposit, withdraw, and balance checking
* Minimum balance enforcement

 3. Bank Class

* Holds all accounts (as a dictionary or list)
* Can create, find, and manage multiple accounts
* Handles file saving/loading

Requirements:

* Use @abstractmethod to define abstract methods
* Use property decorators for getters/setters
* Use try-except blocks for error handling
* Save and load accounts from a file using with open()


Sample Output:

--- Welcome to Python Bank ---
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Transfer Money
6. Exit
Enter your choice: 1

Enter name: Alice
Enter opening balance: 5000
Account created successfully! Account No: 1001
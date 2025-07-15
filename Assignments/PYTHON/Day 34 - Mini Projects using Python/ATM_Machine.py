# Simple ATM Machine Simulation with Exception Handling

balance = 1000  # Starting balance

def display_menu():
    print("\n==== ATM Menu ====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

while True:
    display_menu()
    try:
        choice = int(input("Enter your choice (1-4): "))
        
        if choice == 1:
            print(f"Your balance is: ${balance}")
        
        elif choice == 2:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                balance += amount
                print(f"Deposited ${amount}. New balance: ${balance}")
        
        elif choice == 3:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                print(f"Withdrew ${amount}. New balance: ${balance}")
        
        elif choice == 4:
            print("Thank you for using the ATM. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select 1-4.")

    except ValueError:
        print("Invalid input! Please enter a number.")
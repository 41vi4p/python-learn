# Global variables
balance = 5000
transactions = []
version = 1.4

def withdraw():
    global balance
    try:
        amount = float(input("Enter Amount to Withdraw: "))
        if amount <= 0:
            print("Invalid amount. Please enter a positive number.")
            return
        if amount > balance:
            print("Insufficient funds!")
            return
        balance -= amount
        transactions.append(f"Withdrawn: Rs.{amount:.2f}")
        print(f"Withdrawn Rs.{amount:.2f} successfully.")
        print(f"Current balance: Rs.{balance:.2f}")
    except ValueError:
        print("Please enter a valid number.")

def credit():
    global balance
    try:
        amount = float(input("Enter Amount To Credit: "))
        if amount <= 0:
            print("Invalid amount. Please enter a positive number.")
            return
        balance += amount
        transactions.append(f"Credited: Rs.{amount:.2f}")
        print(f"Credited Rs.{amount:.2f} successfully.")
        print(f"Current balance: Rs.{balance:.2f}")
    except ValueError:
        print("Please enter a valid number.")

def check_balance():
    print(f"\nCurrent Balance: Rs.{balance:.2f}")

def show_transactions():
    print("\n=== Transaction History ===")
    if not transactions:
        print("No transactions yet.")
    else:
        for transaction in transactions:
            print(transaction)

def main():
    while True:
        print("\nWelcome to CRCE Bank v"+str(version)+" by 41vi4p\n")
        print("\n=== CRCE Bank ===\n")
        print("1. Withdraw")
        print("2. Credit")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            withdraw()
        elif choice == '2':
            credit()
        elif choice == '3':
            check_balance()
        elif choice == '4':
            show_transactions()
        elif choice == '5':
            print("\nThank you for using CRCE Bank!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()    
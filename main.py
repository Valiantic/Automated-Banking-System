class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")
            
def main():
    accounts = {}
    
    while True:
        print("/Automated Banking System by Steven Madali")
        
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Account Details")
        print("6. Exit")
        
        choice = input("Enter your choice:")
        
        if choice == "1":
            account_number = len(accounts) + 1
            initial_balance = float(input("Enter initial balance: "))
            accounts[account_number] = Account(account_number, initial_balance)
            print("Account created with number:", account_number)
            
        elif choice == "2":
            account_number = int(input("Enter account number: "))
            account = accounts.get(account_number)
            if account:
                print("Balance", account.balance)
            else:
                print("Account not found.") 
                
        elif choice == "3":
            account_number = int(input("Enter account number: "))
            account = accounts.get(account_number)
            if account:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
                print("Deposited: ", amount)
            else:
                print("Account not found")
                
        elif choice == "4":
            account_number = int(input("Enter account number: "))
            account = accounts.get(account_number)
            if account:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
                print("Withdrawn: ", amount)
            else:
                print("Account not found")
            
                 
        elif choice == "5":
            account_number = int(input("Enter account number: "))
            account = accounts.get(account_number)
            if account:
                print("Account Number: ", account.account_number)
                print("Balance: ", account.balance)
            else:
                print("Account not found")
                
        elif choice == "6":
            print("Exciting...")
            break
        
        else:
                print("Invalid choice. Please try again.")
                
            
if __name__ == '__main__':   
    main()
            
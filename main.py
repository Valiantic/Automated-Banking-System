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
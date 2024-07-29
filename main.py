import speech_recognition as sr #voice recognition para makilala yung boses mo 
import pyttsx3 #text to speech / nagcoconvert ng texto sa salita

# SPEECH GENERATION
def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 145)
    engine.say(text)
    engine.runAndWait()
    
    

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
    
            
            print("Automated Banking System by Steven Madali")
                
            print("1. Create Account")
            print("2. Check Balance")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Account Details")
            print("6. Exit")
                
            choice = input("Enter your choice:")
                
            if choice == "1":
                    account_number = len(accounts) + 1
                    speak("please enter initial balance for your account")
                    initial_balance = float(input("Enter initial balance: "))
                    accounts[account_number] = Account(account_number, initial_balance)
                    print("Account created with number:", account_number)
                    speak("Account Created!")
                    
            elif choice == "2":
                    account_number = int(input("Enter account number: "))
                    account = accounts.get(account_number)
                    if account:
                        print("Balance", account.balance)
                        speak("Here's your current balance on your account ")
                    else:
                        print("Account not found.")
                        speak("Account not found")
                        
            elif choice == "3":
                    account_number = int(input("Enter account number: "))
                    account = accounts.get(account_number)
                    if account:
                        speak("Please enter the amount you want to deposit")
                        amount = float(input("Enter deposit amount: "))
                        account.deposit(amount)
                        print("Deposited: ", amount)
                        speak("Amount has been Deposited!")
                    else:
                        print("Account not found")
                        speak("Account not found")
                        
            elif choice == "4":
                    account_number = int(input("Enter account number: "))
                    account = accounts.get(account_number)
                    if account:
                        speak("Please enter the amount you want to withdraw")
                        amount = float(input("Enter withdrawal amount: "))
                        account.withdraw(amount)
                        print("Withdrawn: ", amount)
                        speak("Money Withdrawed!")
                    else:
                        print("Account not found")
                        speak("Account not found")
                        
                    
                        
            elif choice == "5":
                    account_number = int(input("Enter account number: "))
                    account = accounts.get(account_number)
                    if account:
                        print("Account Number: ", account.account_number)
                        print("Balance: ", account.balance)
                        speak("This is your account details")
                    else:
                        print("Account not found")
                        speak("Account not found")
                        
            elif choice == "6":
                    speak("Thank you for using Automated A.I Banking System!")
                    print("Exiting")
                    break
                
            else:
                        print("Invalid choice. Please try again.")
                        speak("Invalid choice. Please try again.")
                        
                
if __name__ == '__main__':   
    speak("Welcome to Automated A.I Banking System, what can we do for you?")
    print("* Welcome to Automated A.I Banking System, what can we do for you? *\n")
    main()

            
import speech_recognition as sr #voice recognition para makilala yung boses mo 
import pyttsx3 #text to speech / nagcoconvert ng texto sa salita

# SPEECH GENERATION
def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 145)
    engine.say(text)
    engine.runAndWait()
    
    
# COMMAND FUNCTION 
def takecommand():
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source: #mic integration
        speak("Automated A.I Banking System, What can we do for you?")

        r.pause_threshold = 1 # number of seconds to wait
        r.adjust_for_ambient_noise(source) # fpr background noise
        
        audio = r.listen(source, 10, 10) # first second to wait, second is while talking
    
    try:
        print('recognizing....')
        
        query = r.recognize_google(audio, language='en_gb')
        print(f"user said: {query}")
       
    except Exception as e:
        return ""
    
    return query.lower()
    

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
 
def allCommands(message=1):
    
    if message == 1:
        query = takecommand()  #chatfunction
        print(query)
        
    else:
        query = message
            
  
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
                speak("Account Created!")
                
            elif choice == "2":
                account_number = int(input("Enter account number: "))
                account = accounts.get(account_number)
                if account:
                    print("Balance", account.balance)
                    speak("You balance in you account is ", account.balance)
                else:
                    print("Account not found.")
                    speak("Account not found")
                    
            elif choice == "3":
                account_number = int(input("Enter account number: "))
                account = accounts.get(account_number)
                if account:
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                    print("Deposited: ", amount)
                    speak("Money has been Deposited!")
                else:
                    print("Account not found")
                    speak("Account not found")
                    
            elif choice == "4":
                account_number = int(input("Enter account number: "))
                account = accounts.get(account_number)
                if account:
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
                print("Exiting")
                break
            
            else:
                    print("Invalid choice. Please try again.")
                    speak("Invalid choice. Please try again.")
                    
            
if __name__ == '__main__':   
    allCommands()

            
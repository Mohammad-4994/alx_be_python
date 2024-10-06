# Defining the class of bank account 

class BankAccount: 

    def __init__(self):

        self.account_balance = 0 

    def deposit(self):

        amount = input("Enter the amount for deposit: ")

        if amount >= self.account_balance :

            self.account_balance = amount

        else : print ("Invalid ammount , please add valid amount")

    def withdraw(self) : 

        amount = input("Enter the amount for withdraw: ")

        if amount <= self.account_balance : 

            return self.account_balance - amount
        
        else : return False 


    def display_balance(self) :

        print(f"Current Balance: {self.account_balance}") 
    

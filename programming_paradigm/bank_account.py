# Defining the class of bank account 

class BankAccount: 

    def __init__(self,account_balance = 0.00):

        self.account_balance = account_balance

    def deposit(self,amount):

        if amount >= self.account_balance :

            self.account_balance = amount

            return True

        else : 
            
            return False


    def withdraw(self,amount) : 

        if amount > self.account_balance : 

            return False
        
        else : 

            self.account_balance -= amount  

            return True     
       

    def display_balance(self) :

        print("Current Balance: ${:.2f}".format(self.account_balance)) 

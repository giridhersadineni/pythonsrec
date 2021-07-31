class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        return

    def printdetails(self):
        print(f'{self.name} {self.email}')
        return

class UserAccount(User):
    balance=0
    def __init__(self,accountnumber):
        self.accountnumber=accountnumber
        self.balance=0
        return

    def get_balance(self):
        return self.balance
    
    def deposit(self,ammount):
        self.balance+=ammount
        return f"{ammount} Deposited"
    
    def withdraw(self,ammount):
        if self.balance>ammount:
            self.balance-=ammount
            return f'Withdrawed Ammount:{ammount} Available Balance :{self.balance}'
        else:
            return "Insufficient Balance"
        return 

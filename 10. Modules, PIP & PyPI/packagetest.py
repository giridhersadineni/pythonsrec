import mypackage.UserAccount as mp
account=mp.UserAccount(1063)
account.name="Sujay"
account.email="sujay@gmail.com"
account.deposit(2000)
account.printdetails()
print(account.get_balance())

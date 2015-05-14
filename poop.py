# OOP ASSIGNMENT SHELL (Bank Account Manager)

#Your code here for 3 classes
class Accounts(object):
    def __init__ (self, money):
        self.money = money
    def deposit (self, deposit):
        self.money = self.money + deposit
        print (self.money)
    def withdraw (self, withdrawn):
        if self.money >= withdrawn:
            self.money = self.money - withdrawn
            print (self.money)
        elif self.money < withdrawn:
            print ("You do not have enought money to withdraw.")
    def check_balance (self):
        print (self.money)
class Checking (Accounts):
    def withdraw (self, withdrawn):
        withdraw = int (input("How much do you want to withdraw?"))
        if self.money - withdrawn >= 100:
            self.money = self.money - withdrawn
            print (self.money)
        else:
            print ("Not enough funds.")
class Savings (Accounts):
    def interest_earned (self):
        interest = self.money * 0.01
        print (interest)






print("Welcome to Mrs. Leveto's ATM")
accountType = int(input("What type of account? 1:Savings; 2:Checking?"))
if accountType == 1:
    accountPicked = Savings(1500)
elif accountType == 2:
    accountPicked = Checking(1000)


#Your code here - loop asking the user what they want to do.
while accountType == 1:
    savings = int (input ("Would you like to 1: Deposit , 2: Withdraw , 3: Check Balance , 4: Calculate Interest , 5: Exit?"))
    if savings == 1:
        deposit = int (input("How much do you want to deposit?"))
        accountPicked.deposit(deposit)
    elif savings == 2:
        withdraw = int (input("How much do you want to withdraw?"))
        accountPicked.withdraw(withdraw)
    elif savings == 3:
        accountPicked.check_balance()
    elif savings == 4:
        accountPicked.interest_earned()
    elif savings == 5:
        print ("Screw of then, nerd.")
        quit()
while accountType == 2:
        accountPicked.check_balance()
        quit()
        


    
    



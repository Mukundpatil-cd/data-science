

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        
    def deposit(self,amount):
        if amount > 0 :
            self.balance+=amount
            print(f"the {amount} is added , total balance {self.balance}")
        else :
            print("deposit amount should be positive")
            
    def withdraw(self , amount):
        if amount > self.balance:
            print(f"insufficiant balance {self.balance}")
        elif amount <= 0 :
            print("the amount should not be negative or 0")
        else :
            self.balance-=amount
        print(f"the {amount} is withdrawed , the remaining balance is {self.balance}")
        
    def check(self):
        print(f"account balance : {self.balance}")

def main():
    print("welcome to the bank")        
    name = input("enter your name")
    account = BankAccount(name,0)
    
    while True :
        print("1 : deposit")
        print("2 : withdraw")
        print("3 : check")
        print("4 : exit \n ")
        
        c=int(input("enter your choice : "))
        
        if c== 1:
            amount = int(input("enter amount to deposit :"))
            account.deposit(amount)
        elif c==2:
            amount = int(input("enter the amount to withdraw :"))
            account.withdraw(amount)
        elif c==3:
            account.check()
        elif c==4:
            print("thank you for chossing our bank")
            break
        else :
            print("invalid choice")
            
if __name__ == "__main__":
    main()          

        
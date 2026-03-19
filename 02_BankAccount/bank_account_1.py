# Build a class called BankAccount
# It should:
# - Start with a balance of 0
# - deposit(amount) — adds money to the balance
# - withdraw(amount) — removes money, but print "Insufficient funds" if balance is too low
# - get_balance() — returns the current balance
# - str — when printed, shows: "Balance: [amount]"
# Expected:
# account = BankAccount()
# account.deposit(500)
# account.withdraw(200)
# print(account.get_balance()) # 300
# print(account) # Balance: 300
# account.withdraw(400) # Insufficient funds

class BankAccount:
    def __init__ (self):
        self.balance=0
    def deposit(self,amount):
        self.balance+=amount
    def withdraw (self, amount):
        if self.balance >=amount:
         self.balance-=amount
        else:
          print ("Insufficient funds")
    def get_balance (self):
      print(self.balance)
      #return self.balance 
    def __str__ (self):
       print(f"Balance:{self.balance}")


if __name__=="__main__":
  account= BankAccount()
  account.deposit(500)
  account.get_balance()
  account.withdraw(100)
  account.get_balance()
  print(account)

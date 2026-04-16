class BankAccount:
    def __init__(self):
        self.balance = 0                           # account starts with zero

    def deposit(self, amount):
        self.balance = self.balance + amount       # add money to the balance

    def withdraw(self, amount):
        if self.balance < amount:                  # not enough money
            print("Insufficient funds")
        else:
            self.balance = self.balance - amount   # remove money from the balance

    def get_balance(self):
        return self.balance                        # return the current balance


if __name__ == "__main__":
    account = BankAccount()
    account.deposit(500)
    account.withdraw(200)
    print(account.get_balance())   # 300
    account.withdraw(400)          # Insufficient funds
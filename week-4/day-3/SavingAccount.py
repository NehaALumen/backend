from BankAccount import BankAccount
class SavingsAccount(BankAccount):
    
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate=interest_rate
    
    def add_interest(self):
        interest= self.get_balance() * self.interest_rate
        self.set_balance(interest+self.get_balance())
        print(f"${interest} added to the account balance")
        print(f"new balance: ${self.get_balance()}")

travis = SavingsAccount("Travis", 2340000, .05)
print(travis.get_balance())
travis.add_interest()
travis.add_interest()
travis.add_interest()
travis.add_interest()
travis.add_interest()
travis.add_interest()


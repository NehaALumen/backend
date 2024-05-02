class BankAccount():
    def __init__(self, account_holder, balance=0):
        self.__balance=balance
        self.account_holder= account_holder
    
    def get_balance(self):
        return self.__balance
    
    def set_balance(self,new_balance):
        self.__balance=new_balance
    
    def set_account_holder(self, new_achld):
        self.account_holder=new_achld
    
    def get_account_holder(self):
        return self.account_holder

    #deposit method
    def deposit(self,money):
        if money >0:
            self.set_balance(self.get_balance()+money)
            print(f"deposited : ${money}")
            print(f"new balance: ${self.get_balance()}")
        else:
            print("invalid deposit")
    
    #withdraw method
    def withdraw(self,amount):
        if amount > 0 and amount<=self.get_balance():
            self.set_balance(self.get_balance()-amount)
            print(f"withdrew : ${amount}")
            print(f"new balance: ${self.get_balance()}")
        elif amount>self.get_balance():
            print("insufficient balance")
        else:
            print("invalid")

'''dylan = BankAccount("Dylan M Katina",12)
print(dylan.get_balance())
print(dylan.get_account_holder())
dylan.deposit(10000000)
dylan.deposit(-1)
dylan.withdraw(100)'''
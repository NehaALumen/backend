#public attributes - accessible from anywhere both inside and outside the class
#private attributes - indicated by a double underscore (dunder) at the begining of the name __attributename, accessible only within the class
#protected attributes - indicated by a single _ and the name and its accessible in the parent and child class
class Smartphone():
    def __init__(self,model,credit_card,os):
        self.model=model
        self.__wallet=credit_card
        self._os=os
    def show_info(self):
        print(f"model = {self.model}")
        print(f"wallet = *****")
        print(f"OS : {self._os}")
    def get_wallet(self): #getter functions dont take anything other than the current object
        return self.__wallet
    def set_wallet(self, new_card):
        print(f"setting new credit card ending in {new_card[4:]}")
        self.__wallet=new_card


iphone=Smartphone('15 Pro Max','123457','IOS 27')
iphone.show_info()
print(iphone.model)
#print(iphone.__wallet) - will give an error because its private

#getters and setters
print(iphone.get_wallet())
print(iphone.set_wallet('0987653'))
print(iphone.get_wallet())
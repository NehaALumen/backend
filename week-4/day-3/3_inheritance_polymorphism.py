class User():
    def __init__(self, email, pwd, usrnm):
        self.email=email
        self.pwd=pwd
        self.usrnm=usrnm

    def user_info(self):
        print(f"User : {self.usrnm} can be contacted at {self.email}")

    def set_password(self,pwd):
        self.pwd=pwd

class AdminUser(User): #inherits user
    def __init__(self, email, pwd,usrnm,adminid):
        super().__init__(email,pwd,usrnm)
        self.admin_id=adminid
        self.isadmin=True
    def user_info(self): #overriden function from parent
        print(f"Admin #{self.admin_id}: {self.usrnm} can receive support tickets at {self.email}")

billy_bob = User('bb@email.com','pfrfs','billy-b')
billy_bob.user_info()
travis=AdminUser("travispeack@email.com",'12345','travisp',1)
travis.user_info() #inherits this method
travis.set_password('Donkey@12234')
print(travis.pwd)
print(travis.isadmin)
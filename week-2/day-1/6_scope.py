#in python you have 2 kids of scope, global and local
#the scope determines which variables are accessible
#global scope is anywhere outside of your functions

x=7
a ='words'
alist=['item1','item2','item3']
#all above vars are global and can be accessed anywhere in the code

if x:
    print(x)

#local scope is created inside of a function definition

def local_func():
    y=7 #this is a local variable and can only be referenced within this function
    print(x) #global var can be accessed here
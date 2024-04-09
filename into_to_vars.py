#variables are abstract storage locations we associate with a name
food = 'Tacos'
print(food)
food=123
print(food)
name= food
print(name)
name="neha"
print("my name is ", name)
#dynamic typing means variables can be reassigned
# multiple assignement
first , middle , last = 'neha', 'kumari', 'arora'
print(middle)
st,intt,fll = 'neha' , 123 , 3.4
print(st,intt,fll)
#naming convention in python
#variables use snake_case
fav_food= 'sabudana'+'\nvada'
print(fav_food)
#constant variables - a var whose value should never change - use capital SNAKE_CASE
NUM_PI = 3.14
print(NUM_PI)
NUM_PI=5.6 #there is no equivalent to a const keyword in python like in java
print(NUM_PI)
'''naming convention for vars
dont start with numeric values
use snake_case
use ctrl+/ to select a bunch of code and comment it
no special chars other than _ in var names
no keywords
'''
#overriding print
# print = neha is allowed
#can no longer use print

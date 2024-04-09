#type function allows us to see the datatype of any given value
print(type("hello world"))
print(type(9.777777777777777777777777777777777777777777777777777777777777777))
print(type(5))
print(type('5'+'neha'))
# var= 5 + 'neha'
# print(type(var))  - doesnt work
var = 4 +10.5
print(type(var))
#typecasting
var='4'
print(type(int(var)))
print(int(var)) #shows 4 the integer
var= 6.3
print(type(var))
var=int(var)
print(type(var), var)
#floats can run into an overflow error
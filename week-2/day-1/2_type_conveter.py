#type conversion functions str(), int(), float() , bool()
#allows us to convert from 1 datatype to another as long as it is qualifying data
my_str= "5"
print(my_str)
print(type(my_str))

my_int = int(my_str)
print(my_int)
print(type(my_int))

#converting int to float

my_float=float(my_int)
print(my_float)
print(type(my_float))

#converting from float to string

my_str=str(my_float)
print(my_str)
print(type(my_str))

#converting to boolean
my_bool= True
print(my_bool)
print(type(my_bool))

bool_str= str(my_bool)
print(bool_str)
print(type(bool_str))

bool_int = int(my_bool)
print(bool_int)
print(type(bool_int))

num=1
if num:
    print("we have value")

my_num=0
print(bool(my_num))
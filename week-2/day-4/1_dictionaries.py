#dictionaries in python are a datatype to store a collection to store a collection of key value pairs
#features of a dictionary are mutable
#key value pairs : instead of indices pointing to items in a collection we have labels(keys) that point to items (values)
#they are unordered

#features of key-value pairs
#Keys must be unique in the sense 1 key should be 1 value
#keys are typically strings , but it could be any immutable datatype
#values are flexible and can change and be any datatyppe
#you can have duplicate values

#creating dictionaries 
empty_dictionary ={} #use curly braces
#populated dictionary
#syntax  dictionary = {key: value, key2:value2,..}
kitchen = {"drawer":"silver ware","pantry":"snacks","cabinet":"plates"}
print(kitchen)
#accessing the values from dictionary , syntax dictionary[key] returns value associated with that key
print(kitchen["pantry"])

#KeyError - trying to use a key that doesnt exist
#kicthen["fridge"] -- results in an error

# a way to avoid KeyErrors is to use .get
print(kitchen.get("pantry"))
print(kitchen.get("fridge")) #returns none instead of giving a KeyError

#adding a custom message in the event when a bad key is used
print(kitchen.get("fridge"),"bad key")

#we can store keys in variables to be used
#my_key = input("enter the key with which to search :    ")
#print(kitchen[my_key, f'{my_key} is not a key in your dictionary'])

another_dict = {"pwd1": ["neha","nehatinaneha","140413@neha"], "harshpwd":[123, "123@harsh"]}
print(another_dict.get("pwd1"))

#adding a new key
kitchen["fridge"]="cold stuff"
print(kitchen)

#updating a value
kitchen['cabinet']="plates and bowls"

stock ={"oranges":10,'apples':2,'pears':20}
#restock apples
stock["apples"]+=10
print(stock)
#remove rotting pears
stock["pears"]-=5
print(stock)

# .update(key,value) : merges 1 dictionary into another< adds and updates
car={"year":1968, "Make":"Ford", "Model":"Mustang"}
car.update({"color":"green"})
car["transmission"]="auto"
print(car)
car.update({"wheel":4,"engine":"V8","color":"black"})
print(car)

str_car = ' '.join(car)
print(str_car) #only joins keys


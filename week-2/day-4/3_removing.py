dogs= {"huge":"great dane", "large":"german sheperd","medium":"pitt bull","shemedium":"bull dog","small":"dachshund"}
# .pop(key) - removes the key value pair associated with that key, and returns the value
new_home=dogs.pop("small")
print(f"{new_home} is in his new home")
new_home2=dogs.pop("mini","not a category")
print(new_home2)
print(dogs)

# .popitem() : remove the last key value pair and returns the tuple (key,value)
dog= dogs.popitem()
print(dog) #gives a tuple which is the key and the value
print(dogs)

#del dictionary[key] -- delets the key value pair
del dogs['large']
print(dogs)

#del dogs['large'] #will throw a KeyError

#clear() - removes all key value pairs 
dogs.clear()
print(dogs)

#looping over dictionaries 
chips ={"cheetos":"flamin hot","doritos":"cool ranch","takis":"fuego","miss vicky's":"jalapeno"}

#looping over keys of a dictionary
# .keys() : allows us to print the keys
print("major chip brands")
print("----------------")
for chip_key in chips.keys():
    print(chip_key)

#looping over values of a dictionary
# .values()
print("\nflavors")
print("---------------")
for chip_flavor in chips.values():
    print(chip_flavor)

#looping over both the key and value in a dictionary
print("\nMy Favorite Chip brands and Flavors")
print("--------------------------------------")
for key, value in chips.items():
    print(f"My fav {key} flavor is {value}")

dogs ={"Giant":["st bernard","great dane"],"Large":["lab","golden"],"Medium":["bulldog","cocker"],"small":"shihtzu"}
for key,value in dogs.items():
    print(f"{key}: ")
    if isinstance(value,list):
        for v in value:
            print(f"\t{v}")
    else:
        print(f"\t{value}")



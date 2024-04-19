#lists inside dictionaries
pet_names = {"dogs":["fido","oreo","pumpkin","baby","trouble"],
             "cats":["mittens","catkeisha","snowball","fluffy","smokey"],
             "hamster":["cheddars","hamtaro","lightining","hammie"]
             }

print(pet_names["cats"][2])

dogs ={"Giant":["st bernard","great dane"],"Large":["lab","golden"],"Medium":["bulldog","cocker"],"small":"shihtzu"}
for key,value in dogs.items():
    print(f"{key}: ")
    if isinstance(value,list):
        for v in value:
            print(f"\t{v}")
    else:
        print(f"\t{value}")
#dictionary in a list
books = [
    {"Title":"ABC","Author":"EEE","Genre":"VAF"},
     {"Title":"DEF","Author":"FFF","Genre":"fiction"},
      {"Title":"MEM","Author":"GGG","Genre":"fantasy"}
]

#accessing author fff
print(books[0]["Author"])


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
#looping
for book in books:
    for key, value in book.items():
        print(key)
        print(f"\t{value}")

user= {
    "abc@gmail.com":{"username":"neha","pwd":"12345", "likes":["tacos","paneer"]},
    "mm@gmail.com":{"username":"tina","pwd":"12346", "likes":["pizza","tomato"]},
    "ddd@gmail.com":{"username":"tiny","pwd":"12347", "likes":["keylime pie","fruit"]}
}

print(user["mm@gmail.com"]["likes"][1]) #prints tomato 

def login(user_dict):
    while True:
        email=input("email :")
        password=input("password :")
        try:
            user=user_dict[email]
            if password != user["pwd"]:
                raise KeyError("wrong pwd")
        except KeyError as Ve:
            if 'wrong pwd' in str(Ve):
                print("Invalid password")
            else:
                print("Invalid user name")
        else:
            print(f"welcome back {user["username"]}")
            break

login(user)
def addition(a,b):
    return(a+b)

total=addition(3,6)
print(total)


#doubler function, takes in a list of nums and returns a list of doubled nums

def doubler(nums):
    output=[]
    for num in nums:
        output.append(num*2)
    return output
    print("statement after return") #wont print

doubled_list=doubler([5,6,8,99])
print(doubled_list)

#-- no return
def greeting_card(name):
    print(f"have a nice day {name}")

card_message = greeting_card('travis')
print(card_message) #prints none


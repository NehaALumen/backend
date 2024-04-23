#looping over tuples is the exact same as looping over lists

#write a func that loops over a given tuple

def tup_loop(atuple):
    for item in  atuple:
        print(item)

def tup_loop2(atuple):
    for i in range(0,len(atuple)):
        print(atuple[i])
        i+=1

def tup_loop3(atuple):
    i=0
    while i< len(atuple):
        print(atuple[i])
        i+=1

my_tup="apple","banana","orange"
tup_loop(my_tup)
tup_loop2(my_tup)
tup_loop3(my_tup)

#enumerate is a function that allows you to iterate over the index and item at the same time
today="woke up","ate breakfast","walk my dog","prepped lecture","ate luch","graded","meetings", "in class"
for task in enumerate(today):
    print(task) #task is a tuple of the index and the value
    print(f"{task[0]}:{task[1]}") #now you can access the index from the first value of the tuple and the value from the second value of the tuple

for idx, task in enumerate(today):
    print(f"{idx+1}:{task}")


dict1={"k1":"v1","k2":"v2","k3":"v3"}
for key,value in enumerate(dict1): #enumearate can be used with dictionaries too
    print(f"{key}::{value}")

today2=today.__add__(("dinner",))
print(today2)

#nested 
test_tup=(1,2,3,(4,5,6))
for item in test_tup:
    if isinstance(item,tuple) == True:
        print("sub tuple:")
        for item2 in item:
            print(item2)
    else:
        print(item)

print("-------------------------------------------------------")
test_tup2=(1,2,3,{"four":4,"five":5,"six":6},(7,8,9),[10,11,12])
for item in test_tup2:
    if isinstance(item,dict) == True:
        print("sub dict:")
        for item2 in item.values():
            print(item2)
    elif isinstance(item,tuple) == True:
        print("sub tuple:")
        for item2 in item:
            print(item2)
    elif isinstance(item,list) == True:
        print("sub list:")
        for item2 in item:
            print(item2)
    else:
        print(item)
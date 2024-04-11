guest_list =['adam','albert','bob','charlie']
print('bob' in guest_list) #returns boolean
print('neha' in guest_list)
name = input("what's ur name?")
if name in guest_list:
    print("welcome to the party")
else:
    print("scram loser")

#merging lists
list1 = [1,2,3,4]
list2 = [5,6,7,8]
list3= list1+list2
print(list3)

#copying lists using list.copy()
fruit=['apple','orange','kiwi']
copy_fruit = fruit.copy()
print(copy_fruit)
copy_fruit.pop()
print(fruit)
print(copy_fruit)

#copying a list with a full slice
fruit=['apple','orange','kiwi']
copy_fruit = fruit[:]
print(copy_fruit)
copy_fruit.pop()
print(fruit)
print(copy_fruit)

#common mistakes while copying lists
nums=[1,2,3,4]
dnums=nums # here a ref is being set, same memory is being used
print(dnums)
dnums.pop() #affects nums as well
print(dnums)
print(nums)
print(nums is dnums)
fruit=['apple','orange','kiwi']
copy_fruit = fruit[:]
print(fruit is copy_fruit)
print(fruit == copy_fruit)

#list slicing  list[startindex : stopindex] default values for start and stop index is 0 and len(list), slicing returns a sublist or a list object
#stop index is non inclusive
key_lime_pie =['slice1','slice2','slice3','slice4']
my_slice= key_lime_pie[:1]
print(my_slice) #gives ['slice1']
big_slice= key_lime_pie[1:3]
print(big_slice) #gives ['slice2','slice3']
last_slice = key_lime_pie[3:4]
print(last_slice) #gives slice4
print(key_lime_pie[-1]) #gives the last item in the list

#joining a list of strings ''.join(list)

words = ['hello','i','am','getting','joined']
sentence= ''.join(words)
print(sentence) #shows helloiamgettingjoined
proper_sentence = ' '.join(words)
print(proper_sentence) #shows hello i am getting joined
snake_case = '_'.join(words)
print(snake_case) #shows hello_i_am_getting_joined


food = ['tacos','pizza','tiramisu']
print(food)
#list.append(item)
food.append('icecream')
#food[4]='biryani' - wont work
print(food)

# list.insert(idx,item) the index can be out of range too
food.insert(0,'biryani')
print(food)
food.insert(7,'rajma')
print(food)

# list.remove(item) 
#will give ValueError if item doesnt exist
food.remove('pizza')
print(food)

# list.pop(item) removes and returns the last item in the list
freezer= food.pop()
print(food)
print(freezer)

# list.pop(idx)
fridge= food.pop(2)
print(food)
print(fridge)

# list.index(item) - returns the index of the item
print(food.index('icecream'))

#modify values at aparticular position/index
#list[index]=new item
food[2]='gelato'
print(food)

food.append('biryani')
print(food)
# list.count(item)
print(food.count('biryani'))

#list.sort()
food.sort()
print(food)

test_list=[3.14,2,'neha',-1,'aina',6]
#test_list.sort() - will give error
print(test_list)

food.sort(reverse=True)
print(food)

#-----list functions
# len(list) - length of the list
print(len(food))

#sum(list) - sum of items of a numerical list, doesnt work with a list with strings
nums=[1,2,3,4,5,3.0,4.5]
total=sum(nums)
print(total)
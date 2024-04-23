#tuple.count(item): counts the number of times the item exists

shopping ="eggs","milk","creamer","creamer","creamer","creamer","chicken"
print(shopping.count("creamer")) #retruns 4

#len() : gives the length of the tuple
print(len(shopping)) #retruns 7

# tuple.index(item) : shows the index of the first occurence of the item
print(shopping.index("creamer")) # gives 2

#membership checks of a tuple - 'in' is used
print('creamer' in shopping) #retruns ttrue

test_tup=(1,2,3,(4,5,6))
print(5 in test_tup) #returns false
print(5 in test_tup[3]) #return true



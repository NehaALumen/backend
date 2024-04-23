#Tuples are a datatype which is immutable and similar to a list (lists however are mutable)

'''
#characteristics
1. immutable- cant change a tuple without reassigning it
2. ordered - positions can be indexed into
3. like lists they store a variety of objects including duplicate objects 
'''
'''
why bother using a tuple
1. create a collection that will not be changed by you or another dev
2. when iterating over a tuple its faster than a list
3. continous memory is allocated for a tuple unlike a linked list sort of thing which is the case for a list, hence iterating over a tuple is faster
'''
#creating Tuples, we use parens to define a tuple
#empty Tuple
emp_tup=()

singleton = ('element') #singleton is a tuple with one value
print(type(singleton)) #- just prints a string

singleton2=('element',) #has a trailing comma
print(type(singleton2)) #prints tuple

pop_tup = ('this','is','a','populated', 'tuple')
print(type(pop_tup))
print(pop_tup)
str=' '.join(pop_tup)
print(str)

variety_tup =(4,'five',6.0,[7,8,9],{"ten":10})
print(variety_tup)

duple=(True, True, True, False, True, False) #can store duplicate values
print(duple)

#packing tuples : without parens
packed ='tshirt','pants','jacket','socks'
print(packed)
print(type(packed))

#packing variables in tuples
tup_pack =pop_tup, variety_tup, duple
print(tup_pack)

#indexing and slicing tuples
pop_tup = ('this','is','a','populated', 'tuple')
print(pop_tup[3]) #grabs populated
print(pop_tup[1]) #grabs is

variety_tup =(4,'five',6.0,[7,8,9],{"ten":10})
print(variety_tup[3][0])
print(variety_tup[4]["ten"])

print(tup_pack[1][4]["ten"])

#slicing [start:stop] : default start 0, stop - stop is not included 
print(duple[:3]) #getting the first 3 trues out, returns a tuple

list1 = list(duple[:3]) #converting a tuple to a list
print(list1)

#inclass indexing
historical_record=('medieval era',("kinights","castle",("King","Queen")),"reassiance period]")
print(historical_record[1][2][1]) #shows Queen

mythical_collections = ("greek myths",[("Zeus","hera"),["mount olympus",("lighting","thunder")]],"horse myths")
print(mythical_collections[1][1][1][0]) #shows lightining



#immutablity means that the data of a tuple cannot be adjusted in its location in memmory
tup1=(1,2,3,4,5)
print(tup1)
#tup1[3]="four" #gives a type error
#you cant change tuple data in place
#-- small workarounds to change items in tuple
#convert tuple into a list, make changes and convert back to a tuple
tup2=1,2,3,4,5
print(tup2)
print(f"old memory loc : {id(tup2)}")
tup_list=list(tup2)
tup_list[3]="four"
tup2=tuple(tup_list)
print(tup2)
print(f"new memory loc: {id(tup2)}")

#concatenating tuples
tup1=1,2,3,4,5
print(f"{tup1} is now at loc {id(tup1)}")
tup2=6,7,8,9,10
tup1+=tup2
print(f"{tup1} is now at loc {id(tup1)}")

#repeating tuples
short_story='A Tale',
print(short_story)
anthology= short_story*3
print(anthology)
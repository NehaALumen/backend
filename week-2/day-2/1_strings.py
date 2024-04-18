astring ='this is a string with single quotes'
bstring="this is a string with double quotes"
#delimiter  \ backslash
astring ="this is a string\'s string with single quotes"
print(astring)

#strings like lists are immutable, which means you cant change the data that is stored in memory. you can however still reassign

word ="hello"
print(word)
print(id(word)) #id function shows location

word = word + ' world'
print(f"{word} and its location is ", id(word)) #goes into a new location upon reassignment

#indexing in strings, same as lists
name ='Kevin'
second_letter = name[1]
print(second_letter)

#slicing in strings, same as lists list[start:stop] stop is non inclusive
print(name[0:3])
pie='apple pie'
print(pie[0:5])
print(pie[:5]) #same as prev statement
print(pie[6:])

#reverse slice
palindrome = 'tacocat'
reverse = palindrome[::-1]
print(reverse)
#there is a reverse function for lists but not for strings so we use the reverse slice




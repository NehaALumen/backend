#unpacking tuples

#packing tuples reminder
packed ='bacon',"lettuce","tomatoes"
print(f"while its packed, it looks like this {packed}")
#basic unpacking
first, second, third = packed #so cooooooool!!!
print(f"while its unpacked it looks like this {first},{second},{third}")
tup2 = "mayo",
packed+=tup2
#firstt, secondd, thirdd= packed #gives  ValueError: too many values to unpack (expected 3)
#print(f"while its unpacked it looks like this {first},{second},{third}") 

#extended unpacking: takes addition varies values and packs them into a list, use *
enhanced_blt='bacon',"lettuce","tomatoes","mayo","avocado","everything bagel seasoning"
print(enhanced_blt)
first, second, third, *condiments =enhanced_blt
print(first)
print(second)
print(third)
print(condiments) #condiments has all the rest of the staff, condiments comes as a list

enhanced_blt2=('bacon',"lettuce","tomatoes",("mayo","avocado","everything bagel seasoning"))
first, second, third, rest = enhanced_blt2
print(first)
print(second)
print(third)
print(rest)
condi1, condi2, condi3= enhanced_blt2[3]
print(f"{condi1} {condi2} {condi3}")

story ='intro',"conflict","build","bog reveal","climax","conclusion"
beginning ,*middle, fight, end = story #end and fight start from reverse values in the tuple
print(beginning)
print(middle) #notice that when using extended unpacking, the * var returns a list, not a tuple
print(fight)
print(end)


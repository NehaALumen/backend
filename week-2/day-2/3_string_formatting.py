#string formatting allows to embed variables directly into string
#f string
# .format()

#f string
flavor = "Moose Tracks"
food = "ice cream"
statement = f'my favorite {food} flavor is {flavor}'
print(statement)

# .format()
city = "Atlanta"
team = "Falcons"
info = "the {} are from {}".format(team,city)
print(info)

#advanced f strings, embedding full inline expressions
name ='dylan'
greeting= f"hello there{' '+name if name else ''} , how are you doing"
print(greeting)
#string built ins, reminder , strings are immutable, none of these are modifying the original string 

#len() - returns the no, of chars in a string 
phrase = "what's it to you?"
print(len(phrase))

#upper() - returns a full uppercase version of the entire string
phrase="wow its really nice out!"
yell_phrase=phrase.upper()
print(yell_phrase)

#lower() - returns the full lower case version of the entire string
phrase ="Wow look at all these BOOKS!"
inside_voice=phrase.lower()
print(inside_voice)

# title() - formats string in a title case
person ="abraham lincoln"
print(person.title())

# -- replace(substring,replacer,how_many_times=ALL)
am ="good morning morning morning"
pm= am.replace("morning","evening",2)#replaces first 2
print(pm)
pm=am.replace("morning","evening") #replaces all
print(pm)

#strip() removes text from either side of the string, default to remove white space
class_146 = '                        woo this class rocks        '
print(class_146)
print(class_146.strip())

gibbersih="**%$ diamond in the rough ^^&&!!"
print(gibbersih.strip('*$%&^! '))

#lstrip() - strips from the left side
print(gibbersih.lstrip('*$%&^! '))

#rstrip - strips only from the right side
print(gibbersih.rstrip('*$%&^! '))

#find(substring)
jungle='there is a Tiger in my jungle'
tiger=jungle.lower().find('tiger')
print(tiger)

#.count(substring):counts the occurences of the substring in the main string
green= "Green is my fav color, i like green trees, GREEN cars, and green clothing, Green eggs"
print(green.lower().count('green'))

#startwith(substring) - return boolean depdending upon whether the string starts with the substring or not
name1="John fields"
print(name1.lower().startswith('john'))

people = ['Alex',"Aj","Brian","Clinton","Gerardo","Harsh"]
a_team=[]
for student in people:
    if student.lower().startswith('a'):
        a_team.append(student)

print(a_team)

#uninviting the Freys so that its not the red wedding
guest_list =["Rob Stark","Catelyn Stark", "Jorah Mormant", "George Frey", "Arthur Tully"]
#uninvite Freys
new_list=[]
for guest in guest_list:
    if not guest.lower().endswith("frey"):
        new_list.append(guest)
print(new_list)

# -- isalpha : returns True if the string is made entirely of alphabetic characters
letter='A '
print(letter.isalpha())

#-- isdigit()
nums ='123456'
print(nums.isdigit())
age = input("how old are you?")
if age.isdigit():
    age=int(age)
    print(f"on your birthday you will be {age+1}")
else:
    print("you have not eneterd a number")

#isspace() : returns true if string is comprised of only whitespace
#if you're trying to manipulate casing
word = "My Test Variable"
snake_case=''
for letter in word:
    if letter.isspace():
        snake_case+='_'
    else:
        snake_case+=letter.lower()

print(snake_case)

#.split(substring) - splits your string based on a specified substring , into a list of strings, default split on space
words = "This-is-one-big string with many words"
words_list = words.split()
print(words_list)
words_list= words.split('-')
print(words_list)

flavors = input("tell me all of your fav flavors separated by a space").split()
print(flavors)

string1 =['neha','tina','val']
print(str(string1[:2]))

#membership checks in strings using in
magic_word= "blueberry"
sentence = "im having blueberry pancakes for dinner"
if magic_word in sentence:
    print("we got blueberry")

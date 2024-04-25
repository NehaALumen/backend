import re  #re is a package to be imported for using regex functions
# re.findall(pattern, text) - pattern to apply on the text: retrieves all non-overlapping and matches the patterns and returns a list

text1= 'Hi my name is Dylan , and i like to go and do things and stuff'
ands=re.findall(r'and', text1) #literal pattern in an r string
print(ands)

#find all hashtags in a post
post = 'I LOVE # learning #python_is_lyfe and #regex, this is so fun! #coder'
hashtags = re.findall(r'#\w+',post)
print(len(hashtags))
print(hashtags)

#find all words that start with the letter b and end with the letter e
sentence = 'Abe asked to build a bridge but he was told to "beware of a beehives!"'
bez= re.findall(r'\bb\w*e\b',sentence)
print(bez)

#finding emails 
text ='you can contact me at 1dk123@gmail.com or dylan-k2@codingtemple.com, dylan.tina@email.com, priya@test.co'
#username and domain include letters , digits, _,-,.
#domain extensions needs to be onlu 2 or 3 chars
emails = re.findall(r'[\w\.-]+\d*@[\w\.-]+\.[a-z]{2,3}',text)
print(emails)

#re.search(pattern,text) : retruns first occurence of the pattern in a text as a 'match' object
email=input("Enter Email : ")
found = re.search(r'[\w\.-]+\d*@[\w\.-]+\.[a-z]{2,3}\b',email)
print(found) #match object looks like this -- r'[\w\.-]+\d*@[\w\.-]+\.[a-z]{2,3}'
print(found.span())
if found:
    print(f"{found.group} is a valid email")
else:
    print("invalid email")


#Validating phone nums
# 000-000-0000
# 000 000 0000
# 0000000000
print("--------------------------------------")
print("validating phone no.")
number='7708881180'
phone1 = re.search(r'\d{3}(-|\s)?\d{3}(-|\s)?\d{4}',number)
print(phone1)

#re.match(pattern,text) : will retrun a match object if the pattern is at the very begining of the text
text="Hello, World"
obj= re.match(r"Hello",text)
print(obj) #returns match object
print(re.match(r"World",text)) #returns none

#check to see if a website is secure and starts with https
url="https://something.com"
secure=re.match("https",url)
print(f"this site {url} is secure") if secure else print(f"this site {url} is not secure, do you wish to ")

#re.split(pattern,text) splits a text on occurence of pattern and returns a list
text="python,regex;splitting-example. fun, right?"
words = re.split(r"[.,;?\s-]+",text)
print(words)

#re.sub(pattern,replacer,text) : replaces all occurences of a pattern in a string with the replacer in the given text
#now we want to store our phone no. is 0000000000
number="(770)-888-1180"
formatted_number=re.sub(r'\D','',number)
print(formatted_number)

#Anonymous chat
chat =''' 
@Dylan123: "i think i love regex"
@Travis: "dont you have a wife"
@Dylan123: "its just not the same"
@Travis: "She better not see this"
'''
anon_chat = re.sub(r'@\w+',"@user-anon",chat)
print(anon_chat)
print("hello world\ntesting new line"+" testing concatenation\ttesting tab")
print('neha is cool')
print("neha's test")
print('neha says "im awesome"')
#print("neha says "\im awesome"\")
print("neha","tina","harsh","val")
#doc string, multi-line string
print ('''
       1. this option
       2. second option
       3. third option
       ''')
f= open("test.txt","a")
print(''' love to write
      lots of stuff
      blah blah
      ''', file=f)
f.close()
f=open("test.txt","a")
print("\ntest again", file=f)
f.close()
new_text = 'neha is awesome'
f=open("test.txt","a")
print(new_text,file=f)
f.close()
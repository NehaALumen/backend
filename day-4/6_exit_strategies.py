#there are 3 main ways to exit a while loop
#break, false flags, control variable dependent on a state change
#with break
while True:
    fav_food = input("what's ur fav food ? ")
    if fav_food =='tacos':
        print('that is the correct answer.enjoy the fiesta')
        break
    else:
        print('try aagin')

#with flag
searching = True
hours =0
while searching:
    found = input('has anyone found my keys (y/n)? ')
    if found =='y':
        searching=False
    hours+=1
    if not searching:
        print('thankyou for helping me find my keys')
        print('it took us ', hours , ' hours to find')


#with control variable state change
count=0
while count<=10:
    print('running my code')
    count+=1

index=0
alist= ['this','that','the other']
while index < len(alist):
    print('doing ', alist[index])
    index+=1

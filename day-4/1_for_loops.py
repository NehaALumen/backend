''' 
for item in iterable:
    code block

'''
flavors = ['vanilla','choco','mint','caramel']
for flavor in flavors:
    print("running code block")
    print(flavor)

for i in range(0,len(flavors)):
    print(flavors[i])

line =['adam', 'craig', 'dylan','travis','billybob']
guest_list= ['dylan','travis','christian','sarah','soba']
for person in line:
    print(person,' walks up')
    if person in guest_list:
        print("welcome ", person)
    else:
        print('scraam')

nums = [12,344,67,89,90,14,65,22]
count=0
for num in nums:
    if num%2==0:
        print(num , ' is even')
        count+=1
    else:
        print(num, ' is odd')
print('out of ', len(nums),' ',count, ' nos.s are even' )





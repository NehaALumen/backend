num1 = int(input("give me the first number in the range"))
num2 = int(input("give me the second number in the range"))
count=0
for i in range (num1, num2) :
    j=2
    flag=0
    for j in range(j,i) :
        if(i%j==0):
            flag=1

    if(flag==0):
        count+=1

f=open("test.txt","w")
print("the no of prime numbers between ", num1 , "and ", num2, "is ", count,file=f)
print("the nos. are :-",file=f)
for i in range (num1, num2) :
    j=2
    flag=0
    for j in range(j,i) :
        if(i%j==0):
            flag=1

    if(flag==0):
        print(i,file=f)
f.close()


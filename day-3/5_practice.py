test_list=[]
choice='y'
i=0
while(choice=='y'):
    if choice == 'y':
        test_list.append(input('enter string'))
    choice=input('add another ? y/n')
print("list entered :", ' '.join(test_list))
find_str=input("enter the string that u want to remove")
replace_str=input("enter the string that u want to replace it with")
i1=0
while(i1<len(test_list)):
    if test_list[i1] == find_str:
        test_list[i1]=replace_str
    i1+=1

print("new list :", ' '.join(test_list))



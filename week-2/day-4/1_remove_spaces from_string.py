def remove_spaces1(str):
    #str= input("enter a string : ")
    print("removing white spaces")
    str_output=''
    for i in range(0,len(str)):
        if str[i] != ' ':
            str_output+=str[i]
        else:
            pass
    #print(f"string without spaces : {str_output}") 
    return str_output

def remove_spaces2(str2):
    #str2=input("enter a string : ")
    str_list = str2.split(' ')
    #print(str_list)
    str3_output2 = ''.join(str_list)
    #print(str3_output2)
    return str3_output2

def remove_spaces3(str3):
    #str3= input("enter a string : ")
    str_output3 = str3.replace(' ','')
    #print(str_output3)
    return str_output3

print(remove_spaces1(input("enter a string : ")))
print(remove_spaces2(input("enter a string : ")))
print(remove_spaces3(input("enter a string : ")))

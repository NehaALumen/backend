#break, continue, pass

pay_dirt=['dirt','dirt','dirt','gold','dirt','dirt']
for scoop in pay_dirt:
    print('looking for gold')
    if scoop == 'gold':
        print('found gold at position ', pay_dirt.index(scoop))
        break
    else:
        print("found dirt")

nums = [23,45,88,90,3,7,8,23,44]
#program to only sqaure odd nos
#continue
for num in nums:
    if num%2 == 0:
        continue
    num**=2
    print(num)

#pass
my_list = [1,2,3]
for item in my_list:
    pass

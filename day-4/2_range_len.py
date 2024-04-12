#range function creates a sequence of numbers that we can iterate thru
#range(stop) works from 0 to stop, stop is non-inclusive
print(range(10))
print("range to 9")
for num in range(10):
    print(num)

#range(start,stop)
print('range 5-9')
for num in range(5,10):
    print(num)

#range(start,stop,step)
for num in range(9,-1,-1):
    print(num)

alist = ['i1','i2','i3','i4']
for i in range(len(alist)):
    print(alist[i])
    print(i)

for item in alist:
    print(item)
    print(alist.index(item)) #wont work if there are duplicate items in the list


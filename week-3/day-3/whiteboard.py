# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

def arr(a):
    if len(a) ==0 : 
        return a
    cntpst= sum(1 for x in a if x>0)
    negsum = sum(x for x in a if x< 0 )
    return [cntpst,negsum]

l1=[-10,-10,9,8,7,-10]
print(arr(l1))
l2=[]
print(l2)

def minimum(arr):
    arr.sort()
    a1=arr[:1]
    for a in a1:
        return a
               

def maximum(arr):
    arr.sort(reverse=True)
    
    for a in a1:
        return a

arr=[1,2,3,4,5,6,7]
print(maximum(arr))
               

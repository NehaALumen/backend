# var = [<added item> for item in iterable]

students = ['ed','edd','eddy']
shirt_list = ['shirt' for student in students]
print(shirt_list)

students= [1,2,3]
student_double = [num*2 for num in students]
print(student_double)

#list comprehension with an if statement
nums=[1,2,3,4,5,6,7,8]
evens = [num for num in nums if num%2 ==0]
print(evens)

#list comp with if and else
#var = [<if true add item> if <condition> else <else add item> for item in iterable]
grades = [100,98,52,87,90,67]
results = ['pass' if grade >= 70 else 'fail' for grade in grades]
print(results)

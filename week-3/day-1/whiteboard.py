def solution(age):
    try:
        if age <=14:
            return "drink toddy"
        elif age > 14 and age <=18:
            return "drink coke"
        elif age > 18 and age <=21:
            return "drink beer"
        elif age > 21:
            return "drink whisky"
    except:
        print("we ran into an error")

while True:
    try:
        input_age=float(input("please enter your age : "))
        if input_age < 0:
            raise ValueError("not a valid age")
    except ValueError as Ve:
        if 'not a valid age' == str(Ve):
            print("age cannot be negative")
        else:
            print("age should be a valid number")
    else:
        print(f"you can {solution(input_age)}")
        break 



n=12385
m=list(map(int, str(n)))
print(m)
mm=m[::-1]
print(mm)
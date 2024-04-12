nums=[1,2,3,4]
for num1 in nums:
    print("outer loop iteration", num1)
    for num2 in nums:
        print("inner loop iteration", num2)
#2 toppings combination
toppings = ['pepperoni','sausages','ham','pineapple','olives']
for topping1 in toppings:
    for topping2 in toppings:
        if topping1 == topping2:
            print("double", topping2)
        else:
            print(topping1,' ',topping2)
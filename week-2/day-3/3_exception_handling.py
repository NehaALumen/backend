#handling exceptions with Try and Except

#--Try a code block that can potentially raise an exception
#--Except : execute the block if exception occurs 

try:
    x=1
    print(x+'person')
except: #generic except handling
    print("sorry cant do that")


#specific exceptions : to respond with a particular message for a specific message
try:
    div=int(input("give me a no. to divide 10 by: "))
    quotient= 10/div
    print(f"10/{div}={quotient}")
except ZeroDivisionError:
    print("you cant divide by 0")
except ValueError:
    print("enter only nos. please")
except:
    print("invalid input")
finally:
    print("thankyou for providing us with the inputs")

#else : an additional code block that executes when the try block succeeds
while True:
    try:
        age = int(input("how old are you : "))
        birthday= age+1
    except ValueError:
        print("enter numbers only please")
    except:
        print("invalid reposnse")
    else:
        print(f"on your birthday you will be {birthday} years old")
        break

#finally : an additional code block that executes regardless of whether the try block succeeds or not
groceries = ["apple","walnut","pear","bread"]
while True:
    try:
        item = input("which item do you want to remove? ")
        groceries.remove(item)
    except ValueError:
        print("you dont have the item on your list")
    except:
        print("Invalid input")
    else:
        print("successfully removed item")
        break
    finally:
        print("your current list :")
        print("******************")
        for item in groceries:
            print(item)

# raise: raise our own exception
while True:
    print('''
          Choose an action
          ---------------
          1.) Account info
          2.) Settings
          3.)Log Out
''')
    try:
        action = input("Enter action : ")
        if not action in ["1", "2", "3"]:
            raise ValueError
    except ValueError:
        print("Improper value entered, enter 1,2 or 3")
    else:
        if action == '1':
            print("accessing account info")
        elif action == '2':
            print("opening settings")
        elif action =='3':
            print("logging out")
            break

    


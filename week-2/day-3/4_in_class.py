
while True:
    try:
        no_of_books = float(input("enter no. of books to be ordered : "))
        if no_of_books <= 0 :
            raise ValueError("no negative value")
        elif no_of_books/int(no_of_books) != 1:
            raise ValueError("no decimal values")
    except ValueError as Ve:
        if 'no negative value' in str(Ve):
            print("please enter a positive integer, no ngative values")
        elif 'no decimal values' in str(Ve):
            print("please enter a positive integrer, no decimal values")
        else:
            print("please enter digits only")
    else:
        print(f"we will send {int(no_of_books)} to you within 1 week")
        break

    

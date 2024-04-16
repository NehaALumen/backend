#diff types of parameters
#basic parameters :assume their value from the arguments passed
def name_printer(first, last, middle):
    print(f"hello {first} ,{middle}, {last}")
#positional arguments
name_printer('neha','harsh','jaiswal')

# keyword arguments : we explicitly state which parameter takes which value
name_printer(first='neha',middle='harsh', last='jaiswal')

#default parameters : give a param a default value, if none is passed

def tomb_stone(birth,death="TBD"): #assigned default to death
    print(f'''
        This person lived from {birth}  
        to {death}''')
    

tomb_stone("3-24-1986")
tomb_stone("3-24-1986","4-16-2024")
#one thing to note , default params should come  after all non-default basic params

#for example, this wont work :- def breaking(broken=True,working):
#                        pass

#--*args : allows the function to take in an unknonwn no. of arguments brought into the function as a tuple

def vet_hands(staff,*volunteers):
    print(f"on staff today we have {staff[0]} and {staff[1]}")
    if not volunteers:
        print("there are no volunteers to assist today")
    else:
        print("they will be assisted by the following volunteers")
        for vol in volunteers:
            print(vol)

vet_hands(["Dr. Adam","Dr. Eve"],"dylan","neha","travis","pepper")
vet_hands(["Dr. Adam","Dr. Eve"])

# -- **kwargs : unknown amount of keywords, brought into the function as a dictionary
def routine(**daily_events):
    print(daily_events)

routine(morning="wakeup and eat breakfast",mid_morning="walk my dog", afternoon ="prep for today's class", evening="teach class", night="go to sleep")


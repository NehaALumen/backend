#syntax
#def function_name(parameters):
#   code block

#simple function

def greeting():
    print("hello there traveller")

greeting() #call

#function with parameters

def personalized_greeting(name):
    print("hello there  ",name)

personalized_greeting(["neha", "travis","harsh"])
personalized_greeting(6.5004)
personalized_greeting("neha")

#more complex example
#function to give info about coding temple classes

def class_info(instructors, students):
    print("this class is taught by ", instructors[0], instructors[1])
    class_size=len(students)
    print("it has ", class_size , " students")
    for student in students:
        print(student)

instructors_146=["dylan","travis"]
students_146=["neha","tine","tiny","tina","priya"]

class_info(instructors_146,students_146)

instructors_144=["ryan","alex"]
students_144=['billybob',"magic","marshall","lilly"]

class_info(instructors_144,students_144)
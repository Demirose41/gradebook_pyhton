from os import stat


def create() :    
    global user
    print("#"*40)
    t_name = input("Please enter a username\n")
    t_age = input("Please enter your age\n")
    t_grade = input("Please enter grade\n")
    user = dict(name=t_name,age=t_age,grade=t_grade)
    print("User Created")
    state_change(0)

def check(user) :
    print("#"*40)
    for x,y in user.items() :
        print(f"{x} : {y}")
        
    state_change(0) 


def state_change(x):
    global state 
    state = str(x) 
     


def menu() :
    print("Enter your selection \n1.create\n2.check                         9. to exit")
    x = str(input())
    state_change(x)




##While loop '9' will cancel 

state = "0"

user = {}

while state != 'X' :
    print("#"*40)
    if state == "0" :
        print("state 0")
        menu()
        continue
    if state == '1' :
        print("state 1")
        create()
        continue
        
    if state == '2' :
        print("state 2\n")
        check(user)
        continue
            
    if state == 'X':
        break
        
    if state != "0" or 0 or "1" or "2" or "X" :
        print("Invalid input")
        print("#"*40)
        print("#"*40)
        print("#"*40)
        menu()
        
            
        





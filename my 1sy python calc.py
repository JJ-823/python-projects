"""
this is my first atempt at making a (4 function)
python calculator. ive been learning python all
summer of 2025, and i think its time to challenge myself
to see were im at.
started at (10.44am on 9/5/2025)
finished at (2:38pm an 9/5/2025)
took me about 3 hours of working.
"""
def user_input():
    print("pick one of the four functions ")
    print("by putting just one of the four numbers below. ")
    print("adding; = 1 ")
    print("subtracking; = 2")
    print("multiplication; = 3")
    print("division; = 4")
   
    allowed_numbers ={1, 2, 3, 4}


    while True:
        print("choice must be one of the four numbers. ")
        choice = int(input("type the number here: "))
        if choice in allowed_numbers:    
            break


    def if_statements():
        if choice == 1:
            print("type two numbers below.")
            print("the function will be automatically applied ")
            x = int(input("type the (1st) number here: "))
            y = int(input("type the (2nd) number here: "))
            print(x + y)


        elif choice == 2:
            print("type two numbers below.")
            print("the function will be automatically applied ")
            x = int(input("type the (1st) number here: "))      
            y = int(input("type the (2nd) number here: "))
            print(x - y)


        elif choice == 3:
            print("type two numbers below.")
            print("the function will be automatically applied ")
            x = int(input("type the (1st) number here: "))
            y = int(input("type the (2nd)number here: "))
            print(x * y)


        elif choice == 4:
            print("type two numbers below.")
            print("the function will be automatically applied ")
            x = int(input("type the (1st) number here: "))
            y = int(input("type the (2nd)number here: "))
            print(x / y)


    if_statements()
user_input()










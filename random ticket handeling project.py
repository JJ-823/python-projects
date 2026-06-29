"""
complete random project 1.
ticket project.
this is a project/ program that allows user to chose a ticket and get a price out of it.
///
discount code = discount444
///
"""

# used to split lines to make it easier fo user to read.
def line_split ():
    print("""|
|
|
V   """)

def ___main___ ():

    # this function get defined later in the if and elif statements below. --
    def ___final_step___ ():
        value = price
        ticket = type
        # this is a user input for a discounts. --
        line_split()
        discount = (input("(enter a discount code. if you dont want a discount then press enter to continue.): "))  
        line_split()
        # this is if the user uses the right discount code. --
        if discount == "discount444":
            value = price - 5
            print("(you chose to use a discount. you saved $5) ")
            print("(you choose", ticket, " ticket. your total will be $" , value,".) ")
        else:
            #this only happens if the user doesnt use the right discount code. --
            print("(you choose not to use a discount. youll be paying full price.)")
            print("(you choose", ticket, " ticket. your total will be $",value,".) ")
            


    # were caling the line split right here to minimize the clunk within the code. --
    line_split()
    # this is to let the user know the diffrent tickets availibale and ticket values. --
    print("pick what type of ticket you want bye typing the corresponding number") 
    print("((price  =  $5 ) visitor ticket: = 1) ")
    print("((price  =  $5 ) child ticket: = 2) ")
    print("((price  =  $15 ) adult ticket: = 3) ")
    print("((price  =  $10 ) elder ticket: = 4) ")
    print("")



    # the while true just means that if the user doesnt typ the right_ -- 
    # _number then it will keep looping the user input till they put one of the four numbers. --
    while True:
        # this is the first choice.
        choice = (input("(Type the number here. (1, 2, 3, 4)): "))
        # this just mean choice has to be 1, 2, 3, or 4. --
        if choice in ["1", "2", "3", "4"]:
            choice = int(choice)
            break
        else:
            #this happens only if the user doesnt type one of the four numbers. --
            line_split()
            print("(choice must be one of the four numbers.)")
            line_split()
            continue
    


    if choice == 1:
        print (" ( visitors dont get any benefits like discounts. and they wont be able to ride any rides. ) ")
        print(" ( you choose visitor ticket. your total will be $5. ) ") 
        print("")
    
    elif choice == 2:
        price = 5
        type = "child"
        ___final_step___ ()
        print("")

    elif choice == 3:
        price = 15
        type = "adult"
        ___final_step___ ()
        print("")
    
    elif choice == 4:
        price = 10
        type = "elder"
        ___final_step___ ()
        print("")

___main___ ()




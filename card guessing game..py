"""
i havent done a python project in a while. ive been busy with java script/ JS becuase of my AP computer science principles class. 
i did one last python project, i forgot how long ago probably like 2 weeks ago. anyways. i had to stop doing python because i wasnt
letting myself learn (JS) while in (AP csp) i wouldnt ever be able to understand (JS) logic and because of that i always was
one step behinde everyone else so i stoped doing python. while i wasnt doing python, my brain started understanding (JS) and how 
(JS) is more event driven. it took a while until i started my JS project. when doing it, i relized that i understood (JS) logic
all along. i wasnt coding with block like everyone else anymore and i was able to code by hand. while making the project i had a 
error and my teacher was able to catch one of the errors in my code but i found the other one. from then on i finally understood 
how i work when it comes to coding. my brain doesnt work in the way of code.org giving me sample screens that i have to code off of. 
or build off of sample code. my brain couldnt function like that becuase. i strive for creativity so when i sat there working on 
the project. everything that i thought i didnt know clicked. and so for that reason ima celebrate and make this python project.
and the good thing is. is that i didnt forget anything i learned in python. and i still understand the logic.
|
started on 10/9/2025 at 3:16pm
ended on 10/11/2025  at 1:00am

"""



#welcome to my terminal card geussing game.

# these just import diffrent function so the code can work.
import time
import random
import os
clear = lambda: os.system('cls')
clear()



#--


# every variable that is named card then a number is just the picture of the card.
def __card_1 ():
    print("""
        ┌─────────┐  
        │         │ 
        │    1    │ 
        │    ♠    │
        │         │ 
        └─────────┘   
           
    """)
def __card_2 ():
    print("""
        ┌─────────┐  
        │         │ 
        │    2    │ 
        │    ♠    │
        │         │ 
        └─────────┘   
           
    """)


def __card_3 ():
    print("""
        ┌─────────┐  
        │         │ 
        │    3    │ 
        │    ♠    │
        │         │ 
        └─────────┘   
           
    """)
def __card_4 ():
    print("""
        ┌─────────┐  
        │         │ 
        │    4    │ 
        │    ♠    │
        │         │ 
        └─────────┘
           
    """)
def __card_5 ():
    print("""
        ┌─────────┐  
        │         │ 
        │    5    │ 
        │    ♠    │
        │         │ 
        └─────────┘   
           
    """)
def __card_6 ():
    print("""
        ┌─────────┐  
        │         │ 
        │    6    │ 
        │    ♠    │
        │         │ 
        └─────────┘   
           
    """)


# this function holds card pictures all together.
def ___cards___():
    print ("""


    ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ 
    │         │ │         │ │         │ │         │ │         │ │         │
    │    1    │ │    2    │ │    3    │ │    4    │ │    5    │ │    6    │
    │    ♠    │ │    ♠    │ │    ♠    │ │    ♠    │ │    ♠    │ │    ♠    │
    │         │ │         │ │         │ │         │ │         │ │         │
    └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘   
           

 """)


#this helps makes everything easier to read for the user.
def ___line_split___():
    print("""
    |
    |
    V      
        """)

#this is the welcome function. it describes the rules of the game to the user.
def ___welcome___():
    print("""
    """)
    print("(welcome to my card guessing game.) ")
    time.sleep(2)
    print("|")
    print("V")
    print("(rules are simple.) ")
    time.sleep(2)
    print("|")    
    print("V")
    print("(6 cards will be displayed.) ")
    time.sleep(2)
    print("|")
    print("V")
    print("(your goal is to pick the card that holds the desired number value.) ")
    time.sleep(4)
    print("|")
    print("V")
    print("(then you choose the card by typing the number of the card.) ")
    time.sleep(4)
    print("|")
    print("|")
    print("|")
    print("V")

    input("(press enter to continue): ")
    
    #everything above gets put together down here to make the game work.
    def __main_game__():
        #we call a random value 1-100
        value = random.randint(1,100)
        #we set -display- to = -value- so the number can be displayed on screen.  
        display = value
        # -card_value- calls a random number between 1 and 6. 
        card_value = random.choice([1,2,3,4,5,6])
        #this holds the origanl number so it can be displayed on screen.
        card = card_value
        #we set -value- to = the random card number.
        value = card_value
        #this displays the picture of all the cards together.
        ___cards___()        
        print("(what card =", display,")")

        #the whiule true just makes sure the user use one of the six numbers.
        while True:
            print("your guess must be one of the 6 card numebrs.")
            guess = input("(type you guess here):  ")
            ___line_split___()
            if guess in ["1", "2", "3", "4", "5", "6"]:
                guess = int(guess)
                break
            else:
                print("(your guess must be on of the 6 numbers.) ")
                continue

        #if the user guesses the correct card these statements will happen.    
        if guess == value:
            print("(you guessed the correct card!!!) ")   
        
        #if the user guesses the incorrect card this statement will happen.    
        elif guess != value:
            print("(you guessed the wrong number.)") 
            print("(the right card was", card,")" )

        #these if statements will print the picture of the card.    
        if card_value == 1:
            __card_1()
        elif card_value == 2:
            __card_2()
        elif card_value == 3:
            __card_3()
        elif card_value == 4:
            __card_4()
        elif card_value == 5:
             __card_5()
        elif card_value == 6:
            __card_6()
        
        input("(press enter to continue): ")
        
        ___line_split___()
        ___line_split___()
        
        #we ask if the user one of the three choices below.
        print("((1) = play again.) ")
        print("_")
        print("((2) = restart from beginning.) ")
        print("_")       
        print("((3) = stop playing.) ")
        print("_")
        
        #this just means the user input must = 1, 2, or 3.
        while True:
            again = input("(type either 1, 2, or 3): ")
            if again in ["1", "2", "3"]:
                again = int(again)
                break
            else:
                ___line_split___()
                print("((1) = play again. )")
                print("_")
                print("((2) = restart from beginning. )")
                print("_")
                print("((3) = end game. )")
                print("_")
                print("(your choice must be one of the three numbers. )")
                time.sleep(3)
                ___line_split___
                continue
        
        #the first if restats the main the game.
        if again == 1:
             ___line_split___()
             ___line_split___()
             __main_game__()             
        
        #this restarts the game all together.
        elif again == 2:
            ___line_split___()
            ___line_split___()
            ___welcome___()
        
        #this ends the game/ code completely.
        else:
            print(" ")
 
    __main_game__()
___welcome___()






















































"""
welcome to my black jack terminal game. i decided to do this after i had
made a basic card terminal card guessing game.
started on 10/20/2025 at 11:08 pm
ended on 11/14/2025 at 4:18pm

"""

# welcome oto my black jack game.


#---------important stuff i need
import random
import time
import sys
import os
os.system('cls')
first_val = 0
second_val = 0 
user_val = 0
dealer_hand = 0
dealer_val = 0
dealer = ""
user = ""
#-------------
def game_logo():
    print("""

    ╔══════════════════════════════════════════════════════════════════════════════════╗
    ║   ██████╗ ██╗      █████╗  ██████╗██╗  ██╗         ██╗ █████╗  ██████╗██╗  ██╗   ║
    ║   ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝         ██║██╔══██╗██╔════╝██║ ██╔╝   ║
    ║   ██████╔╝██║     ███████║██║     █████╔╝          ██║███████║██║     █████╔╝    ║
    ║   ██╔══██╗██║     ██╔══██║██║     ██╔═██╗     ██   ██║██╔══██║██║     ██╔═██╗    ║
    ║   ██████╔╝███████╗██║  ██║╚██████╗██║  ██╗    ╚█████╔╝██║  ██║╚██████╗██║  ██╗   ║
    ║   ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝   ║
    ╚══════════════════════════════════════════════════════════════════════════════════╝

    """)    

def rule_book_logo():
    print("""
    
    ╔═══════════════════════════════════════════════════════════════════════╗
    ║██████╗ ██╗   ██╗██╗     ███████╗    ██████╗  ██████╗  ██████╗ ██╗  ██╗║
    ║██╔══██╗██║   ██║██║     ██╔════╝    ██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝║
    ║██████╔╝██║   ██║██║     █████╗      ██████╔╝██║   ██║██║   ██║█████╔╝ ║
    ║██╔══██╗██║   ██║██║     ██╔══╝      ██╔══██╗██║   ██║██║   ██║██╔═██╗ ║
    ║██║  ██║╚██████╔╝███████╗███████╗    ██████╔╝╚██████╔╝╚██████╔╝██║  ██╗║
    ║╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝    ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝║
    ╚═══════════════════════════════════════════════════════════════════════╝

    """)

def exit_logo():
    print("""
    
    ╔════════════════════════════════════════════════════════════════════════════════╗
    ║████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗███████╗    ███████╗ ██████╗ ██████╗ ║
    ║╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝██╔════╝    ██╔════╝██╔═══██╗██╔══██╗║
    ║   ██║   ███████║███████║██╔██╗ ██║█████╔╝ ███████╗    █████╗  ██║   ██║██████╔╝║
    ║   ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗ ╚════██║    ██╔══╝  ██║   ██║██╔══██╗║
    ║   ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗███████║    ██║     ╚██████╔╝██║  ██║║
    ║   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝║
    ║                                                                                ║
    ║██████╗ ██╗      █████╗ ██╗   ██╗██╗███╗   ██╗ ██████╗ ██╗██╗██╗                ║
    ║██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██║████╗  ██║██╔════╝ ██║██║██║                ║
    ║██████╔╝██║     ███████║ ╚████╔╝ ██║██╔██╗ ██║██║  ███╗██║██║██║                ║
    ║██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██║██║╚██╗██║██║   ██║╚═╝╚═╝╚═╝                ║
    ║██║     ███████╗██║  ██║   ██║   ██║██║ ╚████║╚██████╔╝██╗██╗██╗                ║
    ║╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝╚═╝                ║
    ╚════════════════════════════════════════════════════════════════════════════════╝

    """)

def home_screen():
    while True:
        os.system('cls')
        game_logo()
        print("")
        print("Type (S) to start or type, (R) for rule book or type (E) to end game. ")
        choice = input("type your choice here: ")
        
        if choice in ["s","S"]:
            os.system('cls')  
            game_logo()
            if __name__ == "__main__":
               game_functions()

        elif choice in ["r","R"]:
            os.system('cls')
            if __name__ == "__main__":
                rule_book()

        elif choice in ["e","E"]:
            os.system('cls') 
            exit_logo()           
            sys.exit(0)

        else:
            os.system('cls')
            print("____you must type one of the choice below.____")
            continue

def rule_book():
    rule_book_logo()
    print(" welcome to my black jack console game. rules are simple. ")
    time.sleep(2)
    print("--- (1) the dealer will have 1 card showing. that card counts towards there overall hand value. -")
    time.sleep(2)
    print("--- (2) then once the dealer gets their card, you will be given your two cards. -- ")
    time.sleep(2)
    print("--- (3) the numbers on both of your cards will count towards your overall hand value. -")
    time.sleep(2)
    print("--- (4) you can choose to either hit to get another card, or stand to keep your current hand. --")
    time.sleep(2)
    print("--- (5) if your total goes over 21, you bust and lose the round. -")
    time.sleep(2)
    print("--- (6) once you stand, the dealer will reveal their hidden card and hit until their total is 17 or higher. --")
    time.sleep(2)
    print("--- (7) whoever is closer to 21 without going over wins the game. -") 
    input("____(press enter to return home)____ ")

def game_functions():
    ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    suits = ["♥","♣","♦","♠"]
    deck = [(rank, suit) for suit in suits for rank in ranks]
    def show_card(rank, suit):
        left_r = f"{rank:<2}"
        right_r = f"{rank:>2}"
        print(f"""
            ┌───────┐
            │{left_r}     │ 
            │   {suit}   │    
            │     {right_r}│        
            └───────┘
            """)    
        
    #makes the first card. it wont paste twice.    

    def dealer_draw():
        global dealer_hand
        global dealer_val

        card = random.choice(deck)
        deck.remove(card)
        rank, suit = card
        show_card(rank, suit)
        if rank == "A":
            dealer_val = random.choice([1,11])
        elif rank in ["J","Q","K"]:
            dealer_val = 10
        else:
            dealer_val = int(rank)
        print("DEALER FIRST CARD VALUE =",dealer_val)
        dealer_hand = dealer_val
    dealer_draw()

    def first_card_maker():
        global first_val
        global user_val

        card = random.choice(deck)
        deck.remove(card)
        rank, suit = card
        show_card(rank, suit)
        if rank in ["J","Q","K"]:
            first_val = 10
        elif rank == "A":
            while True:
                ace_choice = input("(-choose a ace value (1) or (11)-): ")
                if ace_choice == "1":
                    first_val = 1
                    break 
                elif ace_choice == "11":
                    first_val = 11
                    break               
                else:
                    continue 
        else:
            first_val = int(rank)
        print("<--------------------->")
        print("YOUR CARD =",first_val)
        print("<--------------------->")
        user_val = first_val
    first_card_maker()
    
    #this is the second card. it can be used as many times as needed.
    def main_card_maker():
        time.sleep(2)
        global second_val
        global user_val
        card = random.choice(deck)
        deck.remove(card)
        rank, suit = card
        show_card(rank, suit)
        if rank in ["J","Q","K"]:
            second_val = 10
        elif rank == "A":
            while True:
                ace_choice = input("(-choose a ace value (1) or (11)-): ")
                if ace_choice == "1":
                    second_val = 1
                    print("")
                    break 
                elif ace_choice == "11":
                    second_val = 11
                    print("")
                    break                
                else:
                    continue 
        else:
            second_val = int(rank)
        print("<---------------------------------->")
        print("YOUR OTHER CARD VALUE =", second_val)
        user_val = user_val + second_val
        print("<-------------------------->")
        print("YOUR HAND VALUE =", user_val)
        print("<-------------------------->")
        if user_val > 21:
            while True:    
                os.system('cls')
                game_logo()
                print("<--------------------------------------->")
                print("sorry but you went over 21. you lose. ): ")
                print("your hand value was", user_val)
                print("<-------------------->")
                print("(1) = play again. ")
                print("(2) = return home.  ")
                print("(3) = exit game.")    
                print("<-------------------->")
                print("|")
                print("V")
                choice = input("type either (1), (2), or (3) then press enter: ")
                if choice == "1":
                    os.system('cls')
                    game_logo()
                    game_functions()
                
                elif choice == "2":
                    home_screen()

                elif choice == "3":
                    os.system('cls')
                    exit_logo()
                    sys.exit(0)

                else:
                    continue
                    
        #this is the hit or stand function
        def user_draw():
            while True:
                print("type (S) to stand or type (H) to hit. then press enter:  ")
                draw = input("hit or stand: " )
                if draw in ["h","H"]:
                    main_card_maker()
                    break
                elif draw in ["s","S"]:
                    return
                else:
                    continue
        user_draw()    
    main_card_maker()   


    def dealer_draw_2():
        time.sleep(2)
        global dealer_hand
        global dealer_val
        card = random.choice(deck)
        deck.remove(card)
        rank, suit = card
        show_card(rank, suit)
        if rank == "A":
            dealer_val= random.choice([1,11])
        elif rank in ["J","Q","K"]:
            dealer_val = 10
        else:
            dealer_val = int(rank)

        print("DEALER OTHER CARD VALUE =", dealer_val)
        dealer_hand += dealer_val
        if dealer_hand > 21:
            os.system('cls')
            game_logo()
            print("<--------------------------------->")
            print("YOU WIN!!")
            print("dealer went over a card value 21. ")
            print("<--------------------------------->")
            print("(1) = play again. ")
            print("(2) = return home. ")
            print("(3) = exit game. ")    
            print("<----------------->")
            print("|")
            print("V")
            choice = input("type either (1), (2), or (3) then press enter: ")

            if choice == "1":
                os.system('cls')
                game_logo()
                game_functions()

            elif choice == "2":
                os.system('cls')
                home_screen()
                
            elif choice == "3":
                os.system('cls')
                exit_logo()
                sys.exit(0)

            
        elif dealer_hand < 17:
            dealer_draw_2()

        elif dealer_hand >= 17:
            print("<--------------------------------->")
            print("dealer decides to stand")
            print("<--------------------------------->")
            print("|")
            print("V")
            input("___press enter to continue:___ ")
            os.system('cls')
    dealer_draw_2()

    def game_decision_2():
        global dealer_hand
        global dealer_val
        global dealer
        global user
        game_logo()
        while True:
            if user_val == dealer_hand:
                print("<------------------->")
                print("you tied. ")
                dealer = "the dealers hand value =" 
                user = "your hand value ="

            elif user_val > dealer_hand:
                print("<------------------->")
                print("YOU WIN!!! ")
                dealer = "the dealers hand value =" 
                user = "your hand value ="

            elif user_val < dealer_hand:
                print("<------------------->")
                print("you lose ): ")
                dealer = "the dealers hand value =" 
                user = "your hand value ="

            print(dealer, dealer_hand)
            print(user, user_val)
            print("<------------------->")
            print("(1) = play again. ")
            print("(2) = return home. ")
            print("(3) = exit game. ")    
            print("<------------------->")
            print("|")
            print("V")
            choice = input("type either (1), (2), or (3) then press enter: ")
            if choice == "1":
                os.system('cls')
                game_logo()
                game_functions()
            elif choice == "2":
                os.system('cls')
                home_screen()
            elif choice == "3":
                os.system('cls')
                exit_logo()
                sys.exit(0)
            else:       
                continue
    game_decision_2()
# i got rid of the calling of the game function so i can i get the home screen to work
home_screen()







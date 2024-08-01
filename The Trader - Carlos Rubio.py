#Ideas:


def start_menu():
    print("THE TRADER,")
    print("by Carlos Rubio.")
    print("Version 1.1")
    print("A project for the CS-1030 class.")
    input("Press Enter key to start game...")
    ending_count = []
    game(ending_count)
    
def game(ending_count):
        print("")
        inventory = []
        village(ending_count, inventory)
        
def village(ending_count, inventory):
    input("You are a wanderer trader. You have traveled through many countries and continents in search of rare possessions.")
    input("One day, in a little tiny town, you meet a old woman.")
    input("The woman is very nice to you. When you are about to leave, she offers you a mysterious amulet.")
    option_one = input("Do you accept it? (y/n) ")
    while option_one != "y" and option_one !="n":
        print("Please input a valid command.")
        option_one = input("Do you accept it? (y/n) ")
    if option_one == "y":
        inventory.append("mysterious amulet")
        input("You accepted the mysterious amulet.")
    elif option_one == "n":
        input("You did not accepted the mysterious amulet.")
    print("")
    wall(ending_count, inventory)
            
def wall(ending_count, inventory):
    input("A couple of days after talking with the old woman, you leave the village and continue your journeys.")
    input("After wandering for a day or two, you arrive to the capital of the kingdom.")
    input("In the outer walls you meet a guard. He offers you a coat of mail.")
    option_two = input("Do you accept it? (y/n) ")
    while option_two != "y" and option_two != "n":
        print("Please input a valid command")
        option_two = input("Do you accept it? (y/n) ")
    if option_two == "y":
            inventory.append("mail coat")
            input("You accepted the coat of mail.")
    elif option_two == "n":
            input("You did not accepted the coat of mail.")
    print("")
    pub(ending_count, inventory)
            
def pub(ending_count, inventory):
    input("You proceed into the city.")
    input("As you wander in the city, trading here and there, dusk falls. You get into an pub.")
    input('Inside of the pub, you meet a very friendly man. He invites you to come along with him for a "special" trade.') #USING SINGLE APOSTROPHE INSTEAD!!
    option_three = input("Would you go with him? (y/n) ")
    while option_three != "y" and option_three != "n":
        print("Please input avalid command")
        option_three = input("Would you go with him? (y/n) ")
    if option_three == "y":
        input("You decide to accompany him.")
        print("")
        sewerage(ending_count, inventory)
    elif option_three == "n":
        input("You decline the offering.")
        input("After resting for a while, you decide to visit the church.")
        print("")
        church(ending_count, inventory)
            
def sewerage(ending_count, inventory):
    input("You move very into the town, to the poor neighboorhoods.")
    input("You follow the man down to the sewerage.")
    if len(ending_count) == 2 and "FOURTH WALL Ending" not in ending_count:
        input("The man turns to you, and looks at you with open wide eyes.")
        input('"This is not the first time you play this game!" He says.')
        input(f'"You have already reached {len(ending_count)} endings in this game! That is awesome!"')
        input(f'"You need {8-len(ending_count)} more to complete the game!" he says"')
        fav_ending = input('"So far, which have been your favorite ending? Just type it here:" ')
        if fav_ending in ending_count:
            if fav_ending != "UFO Ending" and "UFO Ending" not in ending_count:
                input('"Hahahaha! I like that one too!" The man answers. "Wait till you see the UFO Ending!"')
            else:
                input(f'"Hahaha! I like that one too!" The man answers. "Wait till you see the other {8-len(ending_count)}!"')
            print()
        else:
            input("Hmmmm, I don't think that's an ending in this game, but not sure! The developer always changes stuff up!")
        print()
        input("FOURTH WALL ENDING")
        print(inventory)
        if "FOURTH WALL Ending" not in ending_count:
            ending_count.append("FOURTH WALL Ending")
    else:
        input("Few minutes in, many men ambush you. It's a trap and they try to stab you to death.")
        if "mail coat" in inventory:
            input("But because of the coat of mail, you survived and escaped to the church.")
            print("")
            church(ending_count, inventory)
        else: #killed ending
            input("You are killed by the many thieves, and they take all your possesions.")
            print()
            print("KILLED ENDING")
            print(inventory)
            if "KILLED Ending" not in ending_count:
                ending_count.append("KILLED Ending")
    print(f"Ending count = {len(ending_count)}/8")
    if len(ending_count)/8 == 1:
        input("Congratulations, you have unlocked all the endings!")
        print("Thank you so much for playing! - Carlos Rubio")
        print("List of endings:", ending_count, sep="/n")
    play_again(ending_count)
        
def church(ending_count, inventory):
    print("The father is there. You talk with him.")
    if "DEMON Ending" in ending_count:
        input("The father asks you if you want to join the priesthood and serve the Church.")
        join_clerk = input("Do you accept? (y/n) ")
        if join_clerk == "y": #CLERK Ending
            input("You decided to join the clerk and leave behind your life as a trader.")
            print()
            input("CLERK ENDING")
            print(inventory)
            if "CLERK Ending" not in ending_count:
                ending_count.append("CLERK Ending")
            if len(ending_count)/8 == 1:
                input("Congratulations, you have unlocked all the endings!")
                print("Thank you so much for playing! - Carlos Rubio")
                print("List of endings:", ending_count, sep="/n")
            play_again(ending_count)
    input("After the conversation, the father leaves the room. You see a shiny crucifix hanging on the altar.")
    option_four = input("Do you take it? (y/n) ")
    while option_four != "y" and option_four != "n":
        print("Please input a valid command.")
        option_four = input("Do you take it? (y/n) ")
    if option_four == "y":
        inventory.append("crucifix")
        print("You took the crucifix.")
    elif option_four == "n":
        print("You did not take the crucifix.")
    print("")
    palace(ending_count, inventory)
            
def palace(ending_count, inventory):
    input("You go to the palace to meet the king.")
    if len(ending_count) == 2 and "FOURTH WALL Ending" not in ending_count: #FOURTH WALL Ending
        input("When the king looks at you, he opens his eyes wide.")
        input('"This is not the first time we meet here!" He says.')
        input(f'"You have already reached  {len(ending_count)} endings in this game!"')
        input(f'"You need {8-len(ending_count)} more to complete the game!" he says"')
        fav_ending = input('"So far, which have been your favorite ending? Just type it next:" ')
        if fav_ending in ending_count:
            if fav_ending != "UFO Ending" and "UFO Ending" not in ending_count:
                input('"Hahahaha! I like that one too!" The king answers. "Wait till you see the UFO Ending!"')
            else:
                input(f'"Hahaha! I like that one too!" The king answers. "Wait till you see the other {8-len(ending_count)}!"')
        else:
            input("Hmmmm, I don't think that's an ending in this game, but not sure! The developer always changes stuff up!")
        print()
        input("FOURTH WALL ENDING")
        print(inventory)
        if "FOURTH WALL Ending" not in ending_count:
            ending_count.append("FOURTH WALL Ending")
                
    elif "mysterious amulet" in inventory and not "crucifix" in inventory: #demon_ending
        input("In the throne, a portal opens. From inside, a hordes of demons appear and raid the castle, killing everybody including you.")
        print()
        input("DEMON ENDING")
        print(inventory)
        if "DEMON Ending" not in ending_count:
            ending_count.append("DEMON Ending")
        
    elif "crucifix" in inventory and not "mysterious amulet" in inventory: #apostle_ending
        input("He sees the crucifix and decides to name you the pope of the kingdom")
        print()
        input("APOSTLE ENDING")
        print(inventory)
        if "APOSTLE Ending" not in ending_count:
            ending_count.append("APOSTLE Ending")
            
    elif "mysterious amulet" and "crucifix" in inventory: #UFO_ending_xDDD
        input("A demon appears and sees the crucifix.")
        input("Suddenly, an UFO appears and kills the demon. Aliens emerge from the UFO.")
        input("The Aliens invite you to join them into sideral space adventures.")
        print()
        print("UFO ENDING")
        print(inventory)
        if "UFO Ending" not in ending_count:
            ending_count.append("UFO Ending")
            
    elif inventory == ["mail coat"]: #promotion ending
        input("He sees you are a great warrior. He recruits you and promotes you to chief general of the kindgom.")
        print()
        input("PROMOTION ENDING")
        print(inventory)
        if "PROMOTION Ending" not in ending_count:
            ending_count.append("PROMOTION Ending")
            
    else: #normal ending
        input("He sees you are a very wise trader. He offers you to help him rule the kingdom.")
        print()
        print("NORMAL ENDING")
        print(inventory)
        if "NORMAL Ending" not in ending_count:
            ending_count.append("NORMAL Ending")
            
    input(f"Ending count = {len(ending_count)}/8")
    if len(ending_count)/8 == 1:
        input("Congratulations, you have unlocked all the endings!")
        print("Thank you so much for playing! - Carlos Rubio")
        print("List of endings:", ending_count, sep="/n")
    play_again(ending_count)
        
def play_again(ending_count):
    play_again = input("Do you want to play again? (y/n) ")
    while play_again != "y" and play_again != "n":
        print("Please input a valid command.")
        play_again = input("Do you want to play again? (y/n)")
    if play_again == "y":
        game(ending_count)
    elif play_again == "n":
        print()
        print("Thank you for playing! You might exit the program or restart it.")
    
start_menu()
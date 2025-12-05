#import all libraries needed
import random
import os
import time
#a variable for the pokenots base health so the pokenot center will know what value to return it to
base_health = 0
#a variable for the pokenots current health so damage can be dealt
health = 0
#a variable for the pokenots attack power
attack = 0
#a variable that will be made true or false whether or not they talk to the npc in the town square
talked_to_npc = False
#a list for the users inventory
inventory = []
#a loop for all the code so the user can play again or exit
while True:
    #define function for clearing terminal
    def clear():
        os.system("cls" if os.name == "nt" else "clear")
    clear()
    #define function for printing text fancy
    def fancy(yo_momma):
        for char in yo_momma:
            print(char,end="")
            time.sleep(.001)
    #Display the title screen and let them start
    title = """
 /$$$$$$$   /$$$$$$  /$$   /$$ /$$$$$$$$ /$$   /$$  /$$$$$$  /$$$$$$$$
| $$__  $$ /$$__  $$| $$  /$$/| $$_____/| $$$ | $$ /$$__  $$|__  $$__/
| $$  \ $$| $$  \ $$| $$ /$$/ | $$      | $$$$| $$| $$  \ $$   | $$   
| $$$$$$$/| $$  | $$| $$$$$/  | $$$$$   | $$ $$ $$| $$  | $$   | $$   
| $$____/ | $$  | $$| $$  $$  | $$__/   | $$  $$$$| $$  | $$   | $$   
| $$      | $$  | $$| $$\  $$ | $$      | $$\  $$$| $$  | $$   | $$   
| $$      |  $$$$$$/| $$ \  $$| $$$$$$$$| $$ \  $$|  $$$$$$/   | $$   
|__/       \______/ |__/  \__/|________/|__/  \__/ \______/    |__/ \n"""
    fancy(title)
    input("Press enter to continue")
    clear()
    #print the welcoming
    welcome = "Hello and welcome to Pokenot! This is a totally original game design, as well as the name not at all being stolen."
    fancy(welcome)
    #get the users name and store it in a variable
    get_name = "\nPlease enter your name"
    fancy(get_name)
    name = input("\n")
    #define the function for the first room
    def starter_room():
        #display the description of the room
        #ask the user which starter they would like to choose
        #set the users stats based off their choice
        description = "Hello and welcome to my lab. I'm Professor Spruce and I'll be giving your first Pokenot to begin your adventure!\nYou can choose from Charman, a fire type lizard, Boolbiesore, a grass type dinosaur, or Squishy, a water type turtle. What one would you like: "
        fancy(description)
        while True:
            starter = input("").capitalize().strip()
            if starter == "Charman":
                base_health = 50
                health = 50
                attack = 10
                break
            elif starter == "Boolbiesore":
                base_health = 60
                health = 60
                attack = 8
                break
            elif starter =="Squishy":
                base_health = 55
                health = 55
                attack = 9
                break
            else:
                womp_womp = "Please double check your spelling or enter a valid option this time:"
                fancy(womp_womp)
                continue
        #let the user leave the room finally
        exit = "Now you're finally ready to begin your adventure! Press enter when you're ready to continue"
        fancy(exit)
        input()
        #return the choice and stats to the rest of the program
        return base_health,health,attack,starter
    #define the function for the path
    def path1():
        #display the description of the path
        description = "As you exit the lab, you enter a beaten old path with not much choice other than to go on ahead. Type yes if you'd like to look around: "
        fancy(description)
        #give them the option to look around(though there wont be anything)
        if input("") == "yes":
            womp_womp = "You look around but can't seen to find anything"
            fancy(womp_womp)
        #let them move to the next area
        exit = "Ready to move on? Press enter when you're ready to continue"
        fancy(exit)
        input()
    #define the function for the shop
    def shop():
        #display the description of the shop
        description = "As you walk into the shop, you see a person behind the counter, presumably the shopkeeper.\nType talk or leave to choose: "
        fancy(description)
        #give them the option to leave or to talk to the npc to buy something
        choice = input("").strip().lower()
        if choice == "talk":
            #if they talk to the npc, they'll realize they have no money and can't buy anything, but the shop owner will give them a free potion anyways
            if "potion" in inventory:
                get_out = "Hey didn't I alrady give you something? Get lost!"
                fancy(get_out)
            else:
                gift_giving = "Hi and welcome to my shop! We sell everything from potions to pokespheres, anything a new trainer would need! What would you like to buy....\nHEY! You don't have any money, do you? Still, take this as a gift"
                fancy(gift_giving)
                #add the gift to the users inventory
                inventory.append("potion")
            #return them to the town square
            town_square()
    #define the function for the pokenot center
    def pokenot_center(sigma):
        if sigma == "choice":
            #display the description of the room
            description = "As you enter the Pokenot Center, you see a woman behind a desk in a nurses outfit. As you approach, she says Hi and welcome to the Pokenot Center! I'm nurse Happy. Type heal, explain, or leave"
            fancy(description)
            #give them the option to heal their pokenots or to talk to the nurse, Nurse Happy
            while True:
                choice = input("").strip().lower()
                #if you heal your pokemon then their health will be fully restored to the base stat
                if choice == "heal":
                    health = base_health
                    yippie = "Alright, your pokenots are all healed up!"
                    fancy(yippie)
                    break
                #nurse happy will explain how the pokenot center works if you talk to her
                elif choice == "explain":
                    explanation = "This is a Pokenot Center, where you can heal all your Pokenot! It's completely free and essential to any trainer! So, type heal, explain, or leave:"
                    fancy(explanation)
                    continue
                elif choice == "leave":
                    bye_bye = "Thank you for visiting the Pokenot Center!"
                    fancy(bye_bye)
                    break
                else:
                    fancy("Please enter something valid! Your choices are heal, explain, or leave.")
                    continue
        else:
            health = base_health
            oh_no = "You took a beating out there. Your Pokenots have been restored to full health and you're free to go!"
            fancy(oh_no)
        return health
    #define the function for the training ground
    def training_field():
        #enemy stats
        enemy_health = 55
        enemy_attack = 9
        #describe the training ground and what they can do there
        description = "You enter the field and see a sign labeled Training Ground and a girl standing on one end. As you approach, she says Hi and welcome to the training ground.\nHere you can practice against me to level up your Pokenots!\nType battle if you'd like to practice battle me or leave"
        fancy(description)
        #give them the option to leave or battle the trainer
        while True:
            choice = input().strip().lower()
            if choice == "battle":
                #if they choose to battle then have them battle
                yippie = "Yes! I haven't had someone to battle in forever, no backing out now!"
                fancy(yippie)
                while True:
                    def enemy_turn():
                        fancy("I attack! Squishy, use spit!")
                        health -= enemy_attack
                        if health <= 0:
                            fancy("Oh no, you lost. You're a loser! How does it feel to lose to a little girl?")
                            pokenot_center("dead")
                        else:
                            user_turn()
                    def user_turn():
                        choose = "Type attack, potion(if you have one), or forfeit"
                        fancy(choose)
                        choice = input().strip().lower()
                        if choice == "attack":
                            enemy_health -= attack
                            enemy_turn()
                        elif choice == "potion":
                            if "potion" in inventory:
                                health += 20
                                enemy_turn()
                            else:
                                womp_womp = "You don't have a potion! Try something else"
                                fancy(womp_womp)
                                user_turn()
                        elif choice == "forfeit":
                            fancy("Too bad, you can't forfeit a trainer battle!")
                            user_turn()
                #if they win then their pokemon will level up and gain more attack and health
                #if they loose then they'll be taken to the pokenot center
            elif choice == "leave":
                #if they choose to leave then return them to town square
                break
            else:
                fancy("Please enter something valid! Your choices are battle or leave")
                continue
    #define the funciton for the town square
    def town_square():
        #display the description of town square
        description = "You walk into the town square and see a sign. Welcome to Pal town! There's a few buildings, a shop and a building labeled Pokenot Center? There's also a field and a person standing around\nEnter shop, center, field, or talk to choose where you'd like to go, or continue if you'd just like to move on:"
        fancy(description)
        while True:
        #get their choice of where they want to go or talk to the npc
            choice = input("").lower().strip()
            if choice == "shop":
                shop()
                continue
            elif choice == "center":
                pokenot_center()
                continue
            elif choice == "field":
                training_field()
                continue
            #if they choose to talk to the npcs then go through the dialogue which will allow them to get a secret later on
            elif choice == "talk":
                dialogue = "Hi, you don't look like you're from around here, welcome to Pal Town! The name's Garey Spruce, I'm the professors grandson.\nLet me give you a little secret. On the path to the Gym, I hid a special gift for anyone to find. Keep an eye out when you get there!"
                fancy(dialogue)
                talked_to_npc = True
                continue
            elif choice == "continue":
                break
            else:
                fancy("Please enter a valid input")
                continue
        exit = "You're ready to move on? Press enter to go when you're ready"
        fancy(exit)
        input()
        return
    #define the function for the second path
        #display the description of the path
        #if they talked to the npc in town square, then give them the option to search a bush where they'll find a secret pokesphere
        #if not then they can just continue on their way to the gym
    #define the function for the first room in the gym
        #display the description of the room and their goal
        #have them solve the puzzle
        #once they beat the puzzle, they can enter the final room
        #make it clear once they enter the final room there's no going back
        #allow them to leave to prepare more or enter
    #define the function for the final room
        #describe the room before the gym leader immediately innitiates battle
        #have them battle
        #if you lose, it says goodbye and you have to restart
        #if you win and you got the pokesphere form earlier, you can capture the gym leader and sell him into slavery
        #ask them to restart or exit
    #display the introduction to the game
    #start them off in the first room
    #make all the basic stats and things as variables for inventory, attack, health
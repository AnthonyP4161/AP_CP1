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
        clear()
        #return the choice and stats to the rest of the program
        return base_health,health,attack,starter
    #define the function for the path
    def path1():
        #display the description of the path
        description = "As you exit the lab, you enter a beaten old path with not much choice other than to go on ahead. Type yes if you'd like to look around, or enter if you don't want to: "
        fancy(description)
        #give them the option to look around(though there wont be anything)
        if input("") == "yes":
            womp_womp = "You look around but can't seen to find anything\n"
            fancy(womp_womp)
        #let them move to the next area
        exit = "Ready to move on? Press enter when you're ready to continue\n"
        fancy(exit)
        input()
        clear()
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
                get_out = "Hey didn't I alrady give you something? Get lost!\n"
                fancy(get_out)
                fancy("Press enter to continue\n")
                input()
            else:
                gift_giving = "Hi and welcome to my shop! We sell everything from potions to pokespheres, anything a new trainer would need! What would you like to buy....\nHEY! You don't have any money, do you? Still, take this as a gift\n"
                fancy(gift_giving)
                #add the gift to the users inventory
                inventory.append("potion")
            #return them to the town square
            clear()
        return inventory
    #define the function for the pokenot center
    def pokenot_center(sigma):
        if sigma == "choice":
            #display the description of the room
            description = "As you enter the Pokenot Center, you see a woman behind a desk in a nurses outfit. As you approach, she says Hi and welcome to the Pokenot Center! I'm nurse Happy. Type heal, explain, or leave: "
            fancy(description)
            #give them the option to heal their pokenots or to talk to the nurse, Nurse Happy
            while True:
                choice = input("").strip().lower()
                #if you heal your pokemon then their health will be fully restored to the base stat
                if choice == "heal":
                    health = base_health
                    yippie = "Alright, your pokenots are all healed up!\n"
                    fancy(yippie)
                    break
                #nurse happy will explain how the pokenot center works if you talk to her
                elif choice == "explain":
                    explanation = "This is a Pokenot Center, where you can heal all your Pokenot! It's completely free and essential to any trainer! So, type heal, explain, or leave: "
                    fancy(explanation)
                    continue
                elif choice == "leave":
                    bye_bye = "Thank you for visiting the Pokenot Center!\n"
                    fancy(bye_bye)
                    break
                else:
                    fancy("Please enter something valid! Your choices are heal, explain, or leave: ")
                    continue
        else:
            health = base_health
            oh_no = "You took a beating out there. Your Pokenots have been restored to full health and you're free to go!\n"
            fancy(oh_no)
        return health
    #define the function for the training ground
    def training_field(base_health,health,attack,starter,invent):
        inventory = [invent]
        #enemy stats
        enemy_health = 55
        enemy_attack = 9
        def user_turn():
            fancy("\nType attack, potion, or forfeit: ")
            choice = input()
            if choice == "attack":
                return "attack"
            elif choice == "potion":
                return "health"
            elif choice == "forfeit":
                fancy("Too bad, you can't forfeit a trainer battle!")
                user_turn()
            else:
                print("Choose a valid option")
                user_turn()
        def enemy_turn(health):
            health-=enemy_attack
            fancy(f"Squishy attacked! your {starter} has {health} remaining!\n")
            return health
        #describe the training ground and what they can do there
        description = "You enter the field and see a sign labeled Training Ground and a girl standing on one end. As you approach, she says Hi and welcome to the training ground.\nHere you can practice against me to level up your Pokenots!\nType battle or leave: "
        fancy(description)
        #give them the option to leave or battle the trainer
        while True:
            choice = input().strip().lower()
            if choice == "battle":
                #if they choose to battle then have them battle
                yippie = "Yes! I haven't had someone to battle in forever, no backing out now!\n"
                fancy(yippie)
                while True:
                    action = user_turn()
                    if action == "attack":
                        enemy_health -= attack
                        if enemy_health <0:
                            fancy("Squishy has fainted!\n")
                            won = True
                            description = "You walk into the town square again\nEnter shop, center, field, or talk to choose where you'd like to go, or continue if you'd just like to move on: "
                            fancy(description)
                            break
                        else:
                            fancy(f"You attacked pikachu! Pikachu now has {enemy_health} health remaining\n")
                    elif action == "health":
                        health += 15
                        print(f"You healed your Pokenot, they now have {health} health left\n")
                        inventory.remove("potion")
                        continue
                    elif action == "forfeit":
                        fancy("Too flipping bad, you can't forfeit a trainer battle!\n")
                        continue
                    else:
                        fancy("Yo, you gotta enter a valid input!\n")
                        continue
                    if health <= 0:
                        fancy("You lost! You're a loser! How does it feel to lose to a little girl? Come back after being patched up!\n")
                        won = False
                    else:
                        health = enemy_turn(health)
                        continue
                    break
                #if they win then their pokemon will level up and gain more attack and health
                if won == True:
                    health+=10
                    attack+=10
                    base_health+=10
                    return health,base_health,attack,starter,inventory,won
                else:
                    health = pokenot_center("dead")
                    return health,base_health,attack,starter,inventory
                #if they loose then they'll be taken to the pokenot center
            elif choice == "leave":
                #if they choose to leave then return them to town square
                description = "You walk into the town square again\nEnter shop, center, field, or talk to choose where you'd like to go, or continue if you'd just like to move on: "
                fancy(description)
                break
            else:
                fancy("Please enter something valid! Your choices are battle or leave: ")
                continue
        clear()
        return base_health,health,attack,starter,inventory
    #define the funciton for the town square
    def town_square(base_health,health,attack,starter,inventory):
        #display the description of town square
        talked_to_npc = False
        description = "You walk into the town square and see a sign. Welcome to Pal town! There's a few buildings, a shop and a building labeled Pokenot Center? There's also a field and a person standing around\nEnter shop, center, field, or talk to choose where you'd like to go, or continue if you'd just like to move on: "
        fancy(description)
        while True:
        #get their choice of where they want to go or talk to the npc
            choice = input("").lower().strip()
            if choice == "shop":
                inventory = shop()
                fancy("You go back to the town square. Your options are shop, center, field or talk: ")
                continue
            elif choice == "center":
                health = pokenot_center("choice")
                fancy("You go back to the town square. Your options are shop, center, field or talk: ")
                continue
            elif choice == "field":
                health,base_health,attack,starter,inventory = training_field(base_health,health,attack,starter,inventory)
                continue
            #if they choose to talk to the npcs then go through the dialogue which will allow them to get a secret later on
            elif choice == "talk":
                dialogue = "Hi, you don't look like you're from around here, welcome to Pal Town! The name's Garey Spruce, I'm the professors grandson.\nLet me give you a little secret. On the path to the Gym, I hid a special gift for anyone to find. Keep an eye out when you get there!\n"
                fancy(dialogue)
                fancy("You go back to the town square. Your options are shop, center, field or talk: ")
                talked_to_npc = True
                continue
            elif choice == "continue":
                break
            else:
                fancy("Please enter a valid input. Your options are shop, center, field, talk, or continue: ")
                continue
        exit = "You're ready to move on? Press enter to go when you're ready\n"
        fancy(exit)
        input()
        clear()
        return health,base_health,attack,talked_to_npc,inventory
    #define the function for the second path
    def path2(talked_to_npc):
        #display the description of the path
        description = "As you leave town, you walk along another beaten old path"
        fancy(description)
        #if they talked to the npc in town square, then give them the option to search a bush where they'll find a secret pokesphere
        if talked_to_npc == True:
            fancy("As you walk, you remember what Garey said. The only place he could have hid something is a bush nearby. You check behind, and sure enough you find a expertball")
            inventory.append("expertball")
            fancy("Press enter to continue\n")
            input()
            clear()
        #if not then they can just continue on their way to the gym
        else:
            fancy("You continue walking along on your way to the gym. Press enter to continue\n")
            input()
            clear()
        return inventory
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

    base_health,health,attack,starter = starter_room()
    path1()
    health, base_health,attack,talked_to_npc,inventory= town_square(base_health,health,attack,starter,inventory)
    inventory = path2(talked_to_npc)
#import all libraries needed
#a loop for all the code so the user can play again or exit
    #define the function for the first room
        #display the description of the room
        #ask the user which starter they would like to choose
        #set the users stats based off their choice
        #let the user leave the room finally
        #return the choice and stats to the rest of the program
    #define the function for the path
        #display the description of the path
        #give them the option to look around(though there wont be anything)
        #let them move to the next area
    #define the funciton for the town square
        #display the description of town square
        #get their choice of where they want to go or talk to the npcs
        #if they choose to talk to the npcs then go through the dialogue which will allow them to get a secret later on
        #go back to the start of this function so they can make a choice again
        #if they choose not to talk to the npcs then move them to the next area they chose
    #define the function for the shop
        #display the description of the shop
        #give them the option to leave or to talk to the npc to buy something
        #if they've already talked to the npc then the npc will kick them out and they will be returned to town square
        #if they talk to the npc, they'll realize they have no money and can't buy anything, but the shop owner will give them a free potion anyways
        #add the gift to the users inventory
        #return them to the town square
    #define the function for the pokenot center
        #display the description of the room
        #give them the option to heal their pokenots or to talk to the nurse, Nurse Happy
        #nurse happy will explain how the pokenot center works if you talk to her
        #if you heal your pokemon then their health will be fully restored to the base stat
        #return them to town square
    #define the function for the training ground
        #describe the training ground and what they can do there
        #give them the option to leave or battle the trainer
        #if they choose to battle then have them battle
        #if they win then their pokemon will level up and gain more attack and health
        #if they loose then they'll be taken to the pokenot center
        #if they choose to leave then return them to town square
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
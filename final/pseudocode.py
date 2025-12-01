"""
 /$$$$$$$   /$$$$$$  /$$   /$$ /$$$$$$$$ /$$   /$$  /$$$$$$  /$$$$$$$$
| $$__  $$ /$$__  $$| $$  /$$/| $$_____/| $$$ | $$ /$$__  $$|__  $$__/
| $$  \ $$| $$  \ $$| $$ /$$/ | $$      | $$$$| $$| $$  \ $$   | $$   
| $$$$$$$/| $$  | $$| $$$$$/  | $$$$$   | $$ $$ $$| $$  | $$   | $$   
| $$____/ | $$  | $$| $$  $$  | $$__/   | $$  $$$$| $$  | $$   | $$   
| $$      | $$  | $$| $$\  $$ | $$      | $$\  $$$| $$  | $$   | $$   
| $$      |  $$$$$$/| $$ \  $$| $$$$$$$$| $$ \  $$|  $$$$$$/   | $$   
|__/       \______/ |__/  \__/|________/|__/  \__/ \______/    |__/  """

#import all libraries needed
#a loop for all the code so the user can play again or exit
    #define the function for the first room
        #print the description of the room
        #ask the user which starter they would like to choose and set stats based of their choice
        #once the user chooses their starter, they will be able to leave the room
        #get their starter choice and which room they chose to go to
    #define the function for the path
        #print the description of the path
        #give them the option to look around(though there wont be anything)
        #let them move to the next area
    #define the funciton for the town square
        #print the description of town square
        #Give them the option to go to any of the buildings or talk to the npcs
        #if they choose to talk to the npcs then go through the dialogue and then call this function again to repeat
        #if they choose not to talk to the npcs then move them to the next area
    #define the function for the shop
        #print the description of the shop
        #give them the option to leave or to talk to the npc to buy something
        #if they've already talked to the npc then the npc will kick them out
        #if they talk to the npc, they'll realize they have no monet and can't buy anything, but the shopkeer will give them a gift anyways
        #add the gift to the users inventory
        #return them to the town square
    #define the function for the pokenot center
        #print the description of the room
        #give them the option to heal their pokenots or to talk to the nurse, Nurse Happy
        #nurse happy will explain how the pokenot center works if you talk to her
        #if you heal your pokemon then their health will be fully restored
        #return them to town square
    #define the function for the training ground
        #describe the training ground and what they can do there
        #give them the option to leave or battle the trainer
        #if they choose to battle then have them battle
        #if they win then their pokemon will level up and gain more attack and health
        #if they loose then they'll be taken to the pokenot center
        #if they choose to leave then allow them to
    #define the function for the second path
        #print the description of the path
        #if they talked to the npc in town square, then give them the option to search a bush where they'll find a secret pokesphere
        #if not then they can just continue on their way to the gym
    #define the function for the first room in the gym
        #print the description of the room and their goal
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
    #print the introduction to the game
    #start them off in the first room
    #make all the basic stats and things as variables for inventory, attack, health


#Changing text color in terminal
    #BLACK = '\033[30m'
    #RED = '\033[31m'
    #GREEN = '\033[32m'
    #YELLOW = '\033[33m'
    #BLUE = '\033[34m'
    #MAGENTA = '\033[35m'
    #CYAN = '\033[36m'
    #WHITE = '\033[37m'
    #RESET = '\033[0m' # Resets to default terminal color

    #print(RED + "This text is red." + RESET)
    #print(GREEN + "This text is green." + RESET)
    #print(BLUE + "This text is blue." + RESET)

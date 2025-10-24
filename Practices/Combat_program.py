#AP 1st Period, Combat Program
import random
while True:

    name = input("First off, what is your name: ").strip().capitalize()
    while True:
        partner = input("Would you like a bulbusaur, squirtle, or charmander: ").strip().capitalize()
        if partner == "Bulbusaur":
            health = 45
            typing = "grass"
            speed = 45
            attack = 17
            defense = 13
            break
        elif partner == "Squirtle":
            health = 44
            typing = "water"
            speed = 43
            attack = 10
            defense = 10
            break
        elif partner == "Charmander":
            health = 39
            typing = "fire"
            speed = 65
            attack = 13
            defense = 7
            break
        else:
            print("Please choose a valid starter")
        enemy_health = 35
        speed = 90
        enemy_attack = 10
        enemy_defense = 10
    print(f"Alrighty {name}, you chose {partner}? {partner}'s stats are as follows:\nHealth:{health}\nType:{typing}\nSpeed:{speed}")
    print("Okay, time for your first battle. You'llbe going against a wild pikachu")
    def user_turn():
        choice = int(input("Would you like to attack(Enter a 1), use a defensive move(Enter a 2), use a potion(Enter a 3), or try to catch it(Enter a 4): "))
        if choice == 1:
            return attack
        elif choice == 2:
            return defense
        elif choice == 3:
            return health + 10
        elif choice == 4:
            catch = random.randint(1,10)
            if catch >= 7:
                return True
            else:
                return False
        else:
            print("Choose a valid option")
            user_turn()

#AP 1st Period, Combat Program
import random
name = input("First off, what is your name: ").strip().capitalize()
while True:
    partner = input("Would you like a Bulbusaur, Squirtle, or Charmander: ").strip().capitalize()
    if partner == "Bulbusaur":
        health = 45
        speed = 45
        attack = 17
        break
    elif partner == "Squirtle":
        health = 44
        speed = 43
        attack = 10
        break
    elif partner == "Charmander":
        health = 39
        speed = 65
        attack = 13
        break
    else:
        print("Please choose a valid starter")
enemy_health = 35
enemy_speed = 43
enemy_attack = 10

print(f"Alrighty {name}, you chose {partner}? {partner}'s stats are as follows:\nHealth:{health}\nSpeed:{speed}\nAttack:{attack}")
print("Okay, time for your first battle. You'll be going against a wild pikachu")

while True:
    def user_turn():
        choice = int(input("Would you like to attack(Enter a 1) use a potion(Enter a 2), or try to catch it(Enter a 3): "))
        if choice == 1:
            return "attack"
        elif choice == 2:
            return "health"
        elif choice == 3:
            catch = random.randint(1,10)
            if catch >= 7:
                return True
            else:
                return False
        else:
            print("Choose a valid option")
            user_turn()

    def enemy_turn(health):
        health -= enemy_attack
        print(f"Pikachu attacked! You have {health} health remaining")
        return health
    if speed >= enemy_speed:
        action = user_turn()
        if action == "attack":
            enemy_health -= attack
            if enemy_health <0:
                print("Pikachu has fainted!")
                break
            else:
                print(f"You attacked pikachu! Pikachu now has {enemy_health} health remaining")
        elif action == "health":
            health += 15
            print(f"You healed {partner}, they now have {health} health left")
        else:
            if action == True:
                print("You caught Pikachu!")
                break
            else:
                print("You didn't catch Pikachu")
    if health <= 0:
        print(f"{partner} has fainted!")
        break
    else:
        healthh = enemy_turn(health)
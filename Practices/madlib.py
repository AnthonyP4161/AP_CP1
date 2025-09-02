#AP 1st Period, Mad Lib

print("Welcome to the MadLib program!")

def quiz():
    #variables
    object = input("Please input an object that can be carried easily, EX. box: ")
    car = input("Please input a type of car, EX. Bugatti: ")
    verb = input("Please input an action ending in -ing, EX. jumping: ")
    city = input("Please input a city name, EX. New York City: ")
    adjective = input("Please input an adjective, EX. spiky: ")

    #printing
    print(" There once was a guy named Bob, who owned a "+object+".\n Bob loved his "+object+" very much.\n Bob purchased his "+object+" just the other day, when he drove to a store in "+city+" in his "+car+".\n Bob was so happy that he started "+verb+" from the sheer amount of joy he felt.\n Bob then immediately left "+city+" and drove home in his "+car+".\n He started looking at his "+object+"even closer, and realized it was "+adjective+"!\n")
    
    #loop
    quiz()
quiz()
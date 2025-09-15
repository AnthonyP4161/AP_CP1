#AP 1st Period, Crew Shares

print("The crew earned a whole bunch of money on the last outing, but the captain(you)\ndidn't have time to divvy it all up before releasing everyone to port. You gave\neach member of the crew 500 dollars for the evening and then sat down with your\nfirst mate to properly divide the shares. ")
earnings = int(input("How much money did you earn, enter as just a number EX. 50000: "))
crew = int(input("How many crew members are in your crew, again just enter a number EX. 30: "))
share = earnings/(crew+2)
captain_share = 7*share
first_mate = 3*share
crew_share = share-500
print(f"You earned ${earnings:.2f} and there's {crew} crew members to divide the money between. The captain will get ${captain_share:.2f} and the first mate will recieve ${first_mate:.2f}, well each crew member will get ${crew_share:.2f}.")
#AP 1st Period, Lists Notes
import random
drivers = ["Verstappen","Tsunoda","Leclerc","Hamilton","Norris","Piastri","Russel","Antonelli","Hadjar","Lawson","Albon","Hulkenburg","Sainz","Gasly","Colapinto","Stroll","Alonso","Bortoleto","Bearman","Ocon"]

print(drivers[random.randint(0,19)])
print("The list is",len(drivers), "people long")
print(drivers)
drivers[0] = "THE GOAT FR FR ON GURT NO CAP SKIBIDI SIGMA"
print(drivers)
drivers[1:2] = ["Lil guy", "Banana Leclerc"]
print(drivers)
#drivers.pop(3)
drivers.remove("Leclerc")
print(drivers)
drivers.insert(3, "Leclerc")
#drivers.extend(["Ohio", "Among Us"])
print(drivers)






print(random.choice(drivers,weights=(4,4,24,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4), k=20))
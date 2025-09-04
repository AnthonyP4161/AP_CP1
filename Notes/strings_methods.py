#AP 1st Period, Strings Methods Notes

subject = "computer programming 1"
subject1 = "COMPUTER PROGRAMMING 1"
subject2 = "cOMPUTER pROGRAMMING 1"
subject3 = "                   Computer Programming 1                          "
subject4 = "CoMpUtEr PrOgRaMmInG 1"

print(subject.title())#CAPITALIZES FIRST LETTER OF EVERY WORD
print(subject.capitalize())#CAPITALIZES FIRST LETTER OF FIRST WORD
print(subject.upper())#ALL LETTERS CAPITALIZED
print(subject1.lower())#ALL LETTERS LOWERCASE
print(subject3.strip())#REMOVES EXTRA SPACES FROM END AND BEGINNING
print(subject4.swapcase())#SWAPS UPPERCASE WITH LOWERCASE

#Idiot Proofing

color = input("What is your favorite color: ").strip().lower()
print("Wow, I like", color, "too!")
print("Wow, I like {color} too!".format(color=color))

#F-strings
print(f"Wow, I like {color} too.")

pi = "3.14159"
print(f"We all know that pi is equal to {pi:.5}")

print(pi.isdecimal())
word = "round"
sentence = "The wheels on the bus go round and round..."
print(sentence.find(word))
piece = sentence.find(word)#INDEX OF THE START OF THE WORD

length=len(word)
print(sentence[piece:piece+length])
print(sentence.replace(word, "vroom"))
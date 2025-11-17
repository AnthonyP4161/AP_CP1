#AP 1st period, *Args and **Kwargs Notes

"""def hi(age = 15, name = "Bob", month = "April" ):
    return f"hello {name}, you're {age} years old, you were born in {month}"
print(hi(age = input("What is your age: "), name = input("What is your name: ")))"""

def full_name(**names):
    if 'middle' in names.keys():
        return f"{names['first']} {names['middle']} {names['last']}"
    else:
        return f"{names['first']} {names['last']}"
print(full_name(first="Koro",last="Sensei"))
print(full_name(first="Super",middle="Duper",last="Sigma"))


def summary(**story):
    sum = ""
    if "names" in story.keys():
        sum+= f"{story["names"]} is the main character of this story. "
    if "place" in story.keys():
        sum+= f"The story takes place in {story['place']}. "
    if "conflict" in story.keys():
        sum+= f"The problem is {story['conflict']}."
    return sum
print(summary(names = "Luke Skywalker", place="a galaxy far far away",conflict="hes rizzing his own sister"))
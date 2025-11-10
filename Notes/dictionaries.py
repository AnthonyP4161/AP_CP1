#AP 1st Period, Dictionaries notes

sigma = {
    "name":"Steve",
    "age":67,
    "job":"babysitter",
    "sibling":"good question",
    "children":["Dustin","Mike","Lucas","Max"]
}

print(f"Does he have siblings: {sigma["sibling"]}")
print(sigma.keys())
for key in sigma.keys():
    if key == "children":
        for name in sigma[key]:
            print(f"{sigma["name"]} has a child named {name}")
    else:
        print(f"{key} is {sigma[key]}")
sigma["sibling"] = ["bob","the","builder"]
print(sigma.values())
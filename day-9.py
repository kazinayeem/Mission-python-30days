# day 9

# Python Dictionaries


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

thisdict["model"] = "newmodel"
print(thisdict)
print(type(thisdict))
print(thisdict["year"])
print(thisdict["brand"])
print(thisdict["colors"][0])

print(len(thisdict))

thisdict1 = dict(name="John", age=36, country="Norway")
print(thisdict1)

for x in thisdict1.values():
    print(x)

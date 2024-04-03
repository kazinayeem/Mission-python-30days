# day 11
import json

# Day 11: File handling: reading from and writing to files.

# "a" - Append - will append to the end of the file
#
# "w" - Write - will overwrite any existing content

# create file new

f = open("input.txt", "w")
f.write("lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor")
f.close()


# read file


r = open("input.txt", "r")
print(r.read())

# json data


# Sample JSON data
data = {
    "name": "John Doe 1",
    "age": 30,
    "city": "New York"
}

alluser = []

metadata = open("input.json", "r")
datas = json.load(metadata)

alluser.append(datas)



f = open("input.json", "w")
convert_json = json.dumps(alluser)
f.write(convert_json)
f.close()






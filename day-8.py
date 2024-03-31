# Day 8-9: Tuples and dictionaries: properties, use cases.
# name : kazi Nayeem
# date : 1/04/2004
# day 8

mytuple = ("apple", "banana", "cherry")

print(mytuple[0])
print(mytuple[0:1])
print(mytuple)

print(type(mytuple))

# duplicate tuple


thistuple = ("apple", "banana", "cherry", "apple", "cherry")

if "apple" in thistuple:
    print("apple is in thistuple")

print(thistuple)

# check length
print(len(thistuple))

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

tuple1_mix = ("abc", 34, True, 40, "male")

# update tuple


x = ("apple", "banana", "cherry")

y = list(x)

y[1] = "kiwi"

x = tuple(y)

print(x)

z = ("apple", "banana", "tomato", "orange")

# convert list then change or add anything's


list_z = list(z)

list_z.append("malta")
# remove


list_z.remove("tomato")
print(list_z)
# also we can use del method
print(type(list_z))

tuple_z = tuple(list_z)

print(tuple_z)

# loop in tuple


new_tuple = ("apple", "banana", "tomato", "malta", "mango")

print(new_tuple)

for i in new_tuple:
    print(i)

# loop use range
print("____________________ for  loop _______________________________")

for i in range(len(new_tuple)):
    print(new_tuple[i])

# while loop
print("_________________________while loop __________________________")

i = 0

while i < len(new_tuple):
    print(new_tuple[i])
    i = i + 1

data = list()
data_len = int(input("enter your data len ::  "))

for i in range(data_len):
    d = input(f"Enter your data  {i + 1}  :  ")
    data.append(d)

print(data)

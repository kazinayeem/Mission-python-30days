# day 10

# Day 10: Sets: introduction, operations.


myset = {"apple", "banana", "cherry"}


print(myset)

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)


thisset.remove("banana")
#  add iiems

thisset.add("hello new added")
for x in thisset:
    print(x)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
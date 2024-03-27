# Day 3-4: Control Flow - If statements, loops (for and while)

# Example 4: If statement with multiple conditions
num = 25

if num % 2 == 0 and num % 5 == 0:
    print("Number is divisible by both 2 and 5")
elif num % 2 == 0:
    print("Number is divisible by 2 but not by 5")
elif num % 5 == 0:
    print("Number is divisible by 5 but not by 2")
else:
    print("Number is neither divisible by 2 nor by 5")

# Example 5: Nested loops
for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")

# Example 6: While loop with break and continue
i = 0
while i < 10:
    if i == 5:
        print("Encountered 5, breaking loop")
        break
    elif i % 2 == 0:
        print(f"Skipping {i}")
        i += 1
        continue
    print(i)
    i += 1

print("Loop finished")


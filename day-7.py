# day 7
# Creating a list
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

# Creating an empty list
empty_list = []
print("Empty list:", empty_list)

# Creating a list with different data types
mixed_list = [1, "hello", 3.14, True]
print("Mixed list:", mixed_list)

# Sorting a list
my_list.sort()
print("Sorted list:", my_list)

# Reversing a list
my_list.reverse()
print("Reversed list:", my_list)

# Count occurrences of an element
print("Count of 2 in the list:", my_list.count(2))

# Clearing a list
my_list.clear()
print("Cleared list:", my_list)

# List comprehension to create a list of squares
squares = [x ** 2 for x in range(1, 6)]
print("List of squares:", squares)

# List comprehension with condition
even_squares = [x ** 2 for x in range(1, 6) if x % 2 == 0]
print("Even squares:", even_squares)

# Creating a nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Nested list:", nested_list)

# Accessing elements in a nested list
print("Element at row 2, column 3:", nested_list[1][2])

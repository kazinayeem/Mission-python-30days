# day 6
# Creating a list
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

# Creating an empty list
empty_list = []
print("Empty list:", empty_list)

# Creating a list with different data types
mixed_list = [1, "hello", 3.14, True]
print("Mixed list:", mixed_list)

# Accessing elements using indexing
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# Slicing a list
print("Slice of the list:", my_list[1:4])

# Length of a list
print("Length of the list:", len(my_list))

# Append an element to the list
my_list.append(6)
print("List after append:", my_list)

# Remove an element from the list
my_list.remove(3)
print("List after removal:", my_list)

# Check if an element exists in the list
print("Is 5 in the list?", 5 in my_list)

# Concatenating lists
new_list = my_list + [7, 8, 9]
print("Concatenated list:", new_list)

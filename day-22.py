import numpy as np

# Creating NumPy arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.arange(10)  # Creates an array from 0 to 9
array3 = np.ones((3, 3))  # Creates a 3x3 array filled with ones
array4 = np.zeros((2, 2))  # Creates a 2x2 array filled with zeros

# Array operations
sum_array = array1 + array2  # Element-wise addition
product_array = array1 * 2   # Scalar multiplication
mean_value = np.mean(array1) # Mean of array1

# Indexing and Slicing
print(array1[2])       # Accessing the third element of array1
print(array2[2:5])     # Slicing elements from index 2 to 4 of array2

# Broadcasting
broadcasted_array = array3 + 1  # Broadcasting scalar value 1 to array3

# Universal Functions (ufuncs)
sqrt_array = np.sqrt(array1)  # Square root of each element of array1

# Array Manipulation
reshaped_array = np.reshape(array1, (5, 1))  # Reshaping array1 to a 5x1 array

# Print results
print("array1:", array1)
print("array2:", array2)
print("array3:", array3)
print("array4:", array4)
print("Sum of array1 and array2:", sum_array)
print("Double of array1:", product_array)
print("Mean of array1:", mean_value)
print("Broadcasted array3:", broadcasted_array)
print("Square root of array1:", sqrt_array)
print("Reshaped array1:", reshaped_array)

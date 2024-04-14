# Day 21-25: Data Manipulation and Analysis

import numpy as np
import pandas as pd

# Day 21: NumPy basics: arrays, array operations

# Creating NumPy arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# Array operations
sum_arr = arr1 + arr2
mul_arr = arr1 * arr2

print("NumPy Basics:")
print("Array 1:", arr1)
print("Array 2:\n", arr2)
print("Sum of arrays:\n", sum_arr)
print("Multiplication of arrays:\n", mul_arr)

# Day 23: Pandas basics: Series, DataFrames, manipulation

# Creating a Pandas Series
s = pd.Series([1, 3, 5, np.nan, 6, 8])

# Creating a Pandas DataFrame
dates = pd.date_range('20240101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

# Manipulating DataFrames
df['E'] = np.random

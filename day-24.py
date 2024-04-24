import pandas as pd

# Creating a Series
data = {'A': 10, 'B': 20, 'C': 30}
series = pd.Series(data)
print("Series:")
print(series)
print()

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Gender': ['F', 'M', 'M']}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
print()

# Accessing elements in DataFrame
print("Accessing elements in DataFrame:")
print("First row:")
print(df.iloc[0])
print("Age column:")
print(df['Age'])
print()

# Adding a new column
df['City'] = ['New York', 'Los Angeles', 'Chicago']
print("DataFrame after adding a new column:")
print(df)
print()

# Deleting a column
df.drop('Gender', axis=1, inplace=True)
print("DataFrame after deleting 'Gender' column:")
print(df)

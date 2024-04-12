# Day 19: Functional programming: map, filter, lambda functions


numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))
numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]

strings = ["hello", "world", "python"]
uppercase_strings = map(lambda x: x.upper(), strings)
print(list(uppercase_strings))  # Output: ['HELLO', 'WORLD', 'PYTHON']

words = ["apple", "banana", "orange", "kiwi", "grape"]
filtered_words = filter(lambda x: x[0].lower() not in ['a', 'e', 'i', 'o', 'u'], words)
print(list(filtered_words))  # Output: ['banana', 'kiwi', 'grape']

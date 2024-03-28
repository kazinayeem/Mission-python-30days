# Day 5: Functions - Defining functions, parameters, return statements

# Example 1: Defining a simple function
def greet():
    print("Hello, welcome to Python!")


# Calling the function
greet()


# Example 2: Function with parameters
def greet_with_name(name):
    print(f"Hello, {name}! Welcome to Python!")


# Calling the function with a parameter
greet_with_name("Alice")


# Example 3: Function with default parameter
def greet_with_default(name="Guest"):
    print(f"Hello, {name}! Welcome to Python!")


# Calling the function without providing a parameter
greet_with_default()
# Calling the function with a parameter
greet_with_default("Bob")


# Example 4: Function with return statement
def add_numbers(x, y):
    return x + y


# Calling the function and storing the result in a variable
result = add_numbers(3, 5)
print("Result of addition:", result)

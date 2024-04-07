# day 14
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero!")
    else:
        print("Result:", result)
    finally:
        print("End of divide function")

# Test the divide function
divide(10, 2)
divide(10, 0)

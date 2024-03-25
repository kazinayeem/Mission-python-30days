# Hello world

print("Hello World!")

# This is a comment
# written in
# more than just one line
print("Hello, World!")

# This is a comment
print("Hello, World!")

x = 5
y = "John"
print(x)
print(y)

x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType


t = 5
print(type(t))

# Example	Data Type	Try it
# x = "Hello World"	str
# x = 20	int
# x = 20.5	float
# x = 1j	complex
# x = ["apple", "banana", "cherry"]	list
# x = ("apple", "banana", "cherry")	tuple
# x = range(6)	range
# x = {"name" : "John", "age" : 36}	dict
# x = {"apple", "banana", "cherry"}	set
# x = frozenset({"apple", "banana", "cherry"})	frozenset
# x = True	bool
# x = b"Hello"	bytes
# x = bytearray(5)	bytearray
# x = memoryview(bytes(5))	memoryview
# x = None	NoneType


s = 1
d = 35656222554887711
q = -3255522

print(type(s))
print(type(d))
print(type(q))

# x = 35e3
# y = 12E4
# z = -87.7e100
#
# print(type(x))
# print(type(y))
# print(type(z))


# Python Casting


x = int(1)  # x will be 1
y = int(2.8)  # y will be 2
z = int("3")  # z will be 3

x = float(1)  # x will be 1.0
y = float(2.8)  # y will be 2.8
z = float("3")  # z will be 3.0
w = float("4.2")  # w will be 4.2

# python string

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Code	Result	Try it
# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
# \ooo	Octal value
# \xhh	Hex value


# Boolean Values
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Python Operators

print(10 + 5)

# Operator	Name	Example	Try it
# +	Addition	x + y
# -	Subtraction	x - y
# *	Multiplication	x * y
# /	Division	x / y
# %	Modulus	x % y
# **	Exponentiation	x ** y
# //	Floor division	x // y


# Python Assignment Operators

# Operator   	Example	Same
# =	x = 5	x = 5
# +=	x += 3	x = x + 3
# -=	x -= 3	x = x - 3
# *=	x *= 3	x = x * 3
# /=	x /= 3	x = x / 3
# %=	x %= 3	x = x % 3
# //=	x //= 3	x = x // 3
# **=	x **= 3	x = x ** 3
# &=	x &= 3	x = x & 3
# |=	x |= 3	x = x | 3
# ^=	x ^= 3	x = x ^ 3
# >>=	x >>= 3	x = x >> 3
# <<=	x <<= 3	x = x << 3


# Python Comparison Operators

# Operator	Name	Example	Try it
# ==	Equal	x == y
# !=	Not equal	x != y
# >	Greater than	x > y
# <	Less than	x < y
# >=	Greater than or equal to	x >= y
# <=	Less than or equal to	x <= y


# Python Logical Operators

# Operator	Description	Example	Try it
# and 	Returns True if both statements are true	x < 5 and  x < 10
# or	Returns True if one of the statements is true	x < 5 or x < 4
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)


# Python Identity Operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
#
# Operator	Description	Example	Try it
# is 	Returns True if both variables are the same object	x is y
# is not	Returns True if both variables are not the same object	x is not y
# Python Membership Operators
# Membership operators are used to test if a sequence is presented in an object:
#
# Operator	Description	Example	Try it
# in 	Returns True if a sequence with the specified value is present in the object	x in y
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y
# Python Bitwise Operators
# Bitwise operators are used to compare (binary) numbers:
#
# Operator	Name	Description	Example	Try it
# & 	AND	Sets each bit to 1 if both bits are 1	x & y
# |	OR	Sets each bit to 1 if one of two bits is 1	x | y
# ^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y
# ~	NOT	Inverts all the bits	~x
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2
# Operator Precedence
# Operator precedence describes the order in which operations are performed.
#
# Example
# Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:

print((6 + 3) - (6 + 3))
# Example
# Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions:

print(100 + 5 * 3)
# The precedence order is described in the table below, starting with the highest precedence at the top:
#
# Operator	Description	Try it
# ()	Parentheses
# **	Exponentiation
# +x  -x  ~x	Unary plus, unary minus, and bitwise NOT
# *  /  //  %	Multiplication, division, floor division, and modulus
# +  -	Addition and subtraction
# <<  >>	Bitwise left and right shifts
# &	Bitwise AND
# ^	Bitwise XOR
# |	Bitwise OR
# ==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators
# not	Logical NOT
# and	AND
# or	OR
# If two operators have the same precedence, the expression is evaluated from left to right.
#
# Example
# Addition + and subtraction - has the same precedence, and therefor we evaluate the expression from left to right:

print(5 + 4 - 7 + 3)

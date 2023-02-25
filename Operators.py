#Examples of Operators:-

#Arithmetic Operators:-
x = 10
y = 3

print(x + y)  # Output: 13
print(x - y)  # Output: 7
print(x * y)  # Output: 30
print(x / y)  # Output: 3.3333333333333335
print(x // y)  # Output: 3 (integer division)
print(x % y)  # Output: 1 (modulo operator)
print(x ** y)  # Output: 1000 (exponentiation)

#Comparison Operators:-
x = 5
y = 10

print(x == y)  # Output: False
print(x != y)  # Output: True
print(x < y)  # Output: True
print(x > y)  # Output: False
print(x <= y)  # Output: True
print(x >= y)  # Output: False

#Assignment Operators:-
x = 5

x += 3  # Equivalent to x = x + 3
print(x)  # Output: 8

x -= 2  # Equivalent to x = x - 2
print(x)  # Output: 6

x *= 4  # Equivalent to x = x * 4
print(x)  # Output: 24

x /= 3  # Equivalent to x = x / 3
print(x)  # Output: 8.0

x %= 5  # Equivalent to x = x % 5
print(x)  # Output: 3.0

x **= 2  # Equivalent to x = x ** 2
print(x)  # Output: 9.0

#Logical Operators:-
x = 5
y = 10

print(x < 8 and y > 5)  # Output: True
print(x < 3 or y > 15)  # Output: False
print(not(x < 8 and y > 5))  # Output: False

#Bitwise Operators:-
x = 5
y = 10

print(x & y)  # Output: 0 (bitwise AND)
print(x | y)  # Output: 15 (bitwise OR)
print(x ^ y)  # Output: 15 (bitwise XOR)
print(~x)  # Output: -6 (bitwise NOT)
print(x << 2)  # Output: 20 (bitwise left shift)
print(y >> 1)  # Output: 5 (bitwise right shift)

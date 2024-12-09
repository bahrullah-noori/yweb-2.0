# Demonstrating operator precedence in Python

# Parentheses
print("1. Parentheses:")
result = (3 + 4) * 5
print("(3 + 4) * 5 =", result)  # Output: 35
print()

# Exponentiation
print("2. Exponentiation:")
result = 2 ** 3 ** 2
print("2 ** 3 ** 2 =", result)  # Output: 512 (evaluates as 2 ** (3 ** 2))
print()

# Unary Operators
print("3. Unary operators:")
result = -3 ** 2
print("-3 ** 2 =", result)  # Output: -9 (evaluates as -(3 ** 2))
print()

# Multiplication and Division
print("4. Multiplication and Division:")
result = 10 / 2 * 5
print("10 / 2 * 5 =", result)  # Output: 25.0 (evaluates left to right)
print()

# Addition and Subtraction
print("5. Addition and Subtraction:")
result = 10 - 3 + 2
print("10 - 3 + 2 =", result)  # Output: 9 (evaluates left to right)
print()

# Logical AND and OR
print("6. Logical AND and OR:")
result = True or False and False
print("True or False and False =", result)  # Output: True (AND has higher precedence than OR)
print()

# Relational and Equality Operators
print("7. Relational and Equality Operators:")
result = 5 > 3 == True
print("5 > 3 == True =", result)  # Output: True (evaluates as (5 > 3) and (3 == True))
print()

# Bitwise Operators
print("8. Bitwise Operators:")
result = 5 | 3 & 1
print("5 | 3 & 1 =", result)  # Output: 5 (AND has higher precedence than OR)
print()

# Combining multiple operators
print("9. Combining multiple operators:")
result = (10 + 5) * 2 ** 3 / 4 % 3
print("(10 + 5) * 2 ** 3 / 4 % 3 =", result)  # Output: 1.0
print()

# Explanation for the above:
# (10 + 5) = 15
# 2 ** 3 = 8
# 15 * 8 = 120
# 120 / 4 = 30
# 30 % 3 = 0

print("Note: Always use parentheses for clarity in complex expressions.")

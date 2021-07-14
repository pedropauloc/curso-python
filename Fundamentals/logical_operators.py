print(True or False)
print(7 != 3 and 2 > 3)


#Negation operator - any number other than 0 will be true
print(not True)
print(not False)

# Truth table of AND
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Truth table of OR
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# Truth table of XOR -  It must be one or the other, must be different
print(True != True)
print(True != False)
print(False != True)
print(False != False)

# Caution! - bit a bit
True & True # AND
False | True # OR
True ^ False # XOR

# AND Bit-a-Bit
# 3 = 11
# 2 = 10
# _ = 10
print(3 & 2)

# OR Bit-a-Bit
# 3 = 11
# 2 = 10
# _ = 11
print(3 | 2)

# XOR Bit-a-Bit
# 3 = 11
# 2 = 10
# _ = 11
print(3 ^ 2)


# a little reality - if the goal was hit
balance = 1000
salary = 4000
expense = 2964

# hit = balance > 0 and salary - expense >= 0.2 * salary
positive_balance = balance > 0
controlled_expenses = salary - expense >= 0.2 * salary
hit = positive_balance and controlled_expenses
print(hit)
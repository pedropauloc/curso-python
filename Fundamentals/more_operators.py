# Member Operator
lists = [1, 2, 3, 'Ana', 'Carla']
print(2 in lists)
print('Ana' not in lists)

# Identifier Operator
# With integers the variable store the values
x = 3
y = x
z = 3
print(x is y)
print(y is z)
print(x is not z)


# With lists the variable store the space of memory
list_a = [1, 2, 3]
list_b = list_a # the list_b receive the values of list_a (They point for the same space of memory)
list_c = [1, 2, 3]

print(list_a is list_b)
print(list_b is list_c)
print(list_a is not list_c)
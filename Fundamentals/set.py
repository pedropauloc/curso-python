# Conjuntos
# does not guarantee insertion order
# is not indexed
# does not accept repeated values, are ignored

a = {1, 2, 3}
print(type(a))
# print(a[0]) error
a = set('coddddd3r')
print(a)

print('3' in a, 4 not in a)

print({1, 2, 3} == {3, 2, 1, 3})

# Operations
c1 = {1, 2}
c2 = {2, 3}
print(c1.union(c2)) # Do not change the set, create a new set
print(c1.intersection(c2)) # Do not change the set, create a new set
c1.update(c2) # change the set c1
print(c1)

print(c2 <= c1 ) # c2 is subset of c1? is contained
print(c1 >= c2) # c1 is superset of c2

print({1, 2, 3} - {2}) # diference between sets
print(c1 - c2)

c1 -= {2} # remove the element
print(c1)
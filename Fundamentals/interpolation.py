# replace values within string
# %s - string, %d - integer, %f (%.2f) - float, %r - boolean
from string import Template

name, age = 'Ana', 30

print('Name: %s Age: %d' % (name, age)) # older version
print('Name: {0} Age: {1}'.format(name, age))
print(f'Name: {name} Age: {age}')

s = Template('Name: $name Age: $age')
print(s.substitute(name=name, age=age))



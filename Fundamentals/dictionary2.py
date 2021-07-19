people = {'name': 'Mateus', 'age': 35, 'courses': ['React', 'Docker']}
print(people)

people['age'] = 44
people['courses'].append('Kubernetes')

print(people)
print(people.pop('age')) # it returns and takes the value
print(people)

people.update({'age': 40, 'gender': 'M'})
print(people)

del people['courses']
print(people)

people.clear()
print(people)
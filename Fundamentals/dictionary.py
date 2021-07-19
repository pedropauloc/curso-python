people = {'name': 'Pedro', 'age': 20, 'courses': ['English', 'Portuguese']}

print(people)
print(people['name'])
print(people['age'])
print(people['courses'])
print(people['courses'][1])
# print(people['tags']) error


print(people.keys())
print(people.values())
print(people.items())
print(people.get('age'))
print(people.get('tags'))

print(people.get('tags', [])) # return a default value, in that case [] empty array

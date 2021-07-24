word = 'paralelepipedo'

for letter in word:
    print(letter, end=',')
print('Fim')

approved = ['Rafaela', 'Pedro', 'Renato', 'Maria']
for name in approved:
    print(name)

for position, name in enumerate(approved):
    print(f'{position + 1})', name)

days_week = ('Sunday', 'Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday')

for day in days_week:
    print(f'Today is the day: {day}')


for letter in set('very cool'):  # the set doesn't guarantee order
    print(letter)

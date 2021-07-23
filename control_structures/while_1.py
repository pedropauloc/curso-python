# while True:
#     print('')

from random import randint

informed_number = -1
secret_number = randint(0, 9)

while informed_number != secret_number:
    informed_number = int(input('Enter the number: '))

print('Secret number {} was found'.format(secret_number))
# Straeaming - is reading the file on demand, reads as required.

try:
    archive = open('people.csv')
    for record in archive:
        # .strip() - remove spaces at the beginning and end .strip('a')
        print('Name: {}, Age: {}'.format(*record.strip().split(',')))

# is exuted even if error occurs
finally:
    archive.close()

# *record.split(',') comes with the \n

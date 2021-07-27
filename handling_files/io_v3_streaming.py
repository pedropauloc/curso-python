# Straeaming - is reading the file on demand, reads as required.

archive = open('people.csv')
for record in archive:
    # .strip() - remove spaces at the beginning and end .strip('a')
    print('Name: {}, Age: {}'.format(*record.strip().split(',')))
archive.close()

# *record.split(',') comes with the \n

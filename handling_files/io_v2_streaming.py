# Straeaming - is reading the file on demand, reads as required.

archive = open('people.csv')
for record in archive:
    print('Name: {}, Age: {}'.format(*record.split(',')))
archive.close()

# *record.split(',') comes with the \n

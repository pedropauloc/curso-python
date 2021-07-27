# Straeaming - is reading the file on demand, reads as required.

with open('people.csv') as archive:
    for record in archive:
        print('Name: {}, Age: {}'.format(*record.strip().split(',')))

if archive.closed:
    print('File has already been closed')



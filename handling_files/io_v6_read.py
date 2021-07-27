# Straeaming - is reading the file on demand, reads as required.

with open('people.csv') as archive:
    with open('people.txt', 'w') as output:
        for record in archive:
            people = record.strip().split(',')
            print('Name: {}, Age: {}'.format(*people), file=output)

if archive.closed:
    print('File has already been closed')



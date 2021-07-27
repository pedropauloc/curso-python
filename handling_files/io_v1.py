archive = open('people.csv')
data = archive.read()
archive.close()

for record in data.splitlines():
    print('Name: {}, Age: {}'.format(*record.split(',')))
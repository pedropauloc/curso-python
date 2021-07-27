import csv

with open('people.csv') as input:
    for people in csv.reader(input):
        print('Name: {}, Age: {}'.format(*people))
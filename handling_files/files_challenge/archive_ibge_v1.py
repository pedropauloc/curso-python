import csv

with open('desafio-ibge.csv') as archive:
    for record in archive:
        data = record.strip().split(',')
        print('9: {}, 4: {}'.format(data[8], data[3]))

archive.close()

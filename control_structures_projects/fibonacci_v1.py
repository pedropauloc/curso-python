#!/usr/bin/python3

def fibonacci():
    penultimo = 0
    ultimo = 1
    print(f'{penultimo}, {ultimo}', end=',')
    while True:
        proximo = ultimo + penultimo
        print(f'{proximo}', end=',')
        penultimo = ultimo
        ultimo = proximo


if __name__ == '__main__':
    fibonacci()
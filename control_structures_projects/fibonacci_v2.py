#!/usr/bin/python3

def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    # o end=',' deixa explicito que eu não quero uma quebra de linha
    print(f'{penultimo}, {ultimo}', end=',')
    while ultimo < limite:
        proximo = ultimo + penultimo
        print(proximo, end=',')
        penultimo = ultimo
        ultimo = proximo


if __name__ == '__main__':
    fibonacci(10000)

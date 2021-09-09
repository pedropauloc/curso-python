# unpacking - pegando um dicionario e desempacotando ele passando como parametro
def result_f1(first, second, third):
    print(f'1 -> {first}')
    print(f'2 -> {second}')
    print(f'3 -> {third}')



if __name__ == '__main__':
    podium = {'second':'M. Versappen',
             'first': 'L. Hamilton',
             'third':'S. Vettel'}
            
    result_f1(**podium)
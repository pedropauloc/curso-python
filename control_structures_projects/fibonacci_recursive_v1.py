def fibonacci(amount, sequence=(0, 1)):
    # Importan: Stop condition
    if len(sequence) == amount:
        return sequence
    # the commma shows that it is in fact a tuple, because it has only one value
    # calling the function itself
    return fibonacci(amount, sequence + (sum(sequence[-2:]),))

if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib)

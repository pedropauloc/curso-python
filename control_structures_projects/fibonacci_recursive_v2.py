def fibonacci(amount, sequence=(0, 1)):
    # Importan: Stop condition
    return sequence if len(sequence) == amount else \
        fibonacci(amount, sequence + (sum(sequence[-2:]),))


if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib)




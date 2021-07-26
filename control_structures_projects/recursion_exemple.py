# a functio calling itself is a recursive function.
def printer(max, current):
    if current >= max:
        return
    print(current)
    printer(max, current + 1)

# printer(10, 1)

# pay attention to the stop condition


''' ERROR
def printer(max, current):
    # if current < max:
    print(current)
    printer(max, current + 1)

# RecursionError: maximum recursion depth exceeded while calling a Python object
'''

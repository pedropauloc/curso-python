# Callable = 'Passivel de ser chamado'
# If you pass a function as a parameter to another function it is possible to execute it.
def exec(fun):
    if callable(fun):
        fun()

def good_morning():
    print('Good Morning!')

def good_evening():
    print('Good Evening!')

if __name__ == '__main__':
    exec(good_morning)
    exec(good_evening)
    # exec(1) Int object is not callable '1()'
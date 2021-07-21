# receiving the values ​​through the terminal
from math import pi
import sys
 

def help():
    print('it is necessary to inform the radius of the circle.')
    print(f'Syntax: {sys.argv[0]} <radius>')


def circle(radius):
    return pi * float(radius) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()

    else:
        radius = sys.argv[1]
        area = circle(radius)
        print('Circle area:', area)

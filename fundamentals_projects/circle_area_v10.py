# receiving the values ​​through the terminal
from math import pi
import sys

def circle(radius):
    return pi * float(radius) ** 2


if __name__ == '__main__':
    # print(sys.argv[1]) # taking the past agruments
    radius = sys.argv[1]
    area = circle(radius)
    print('Circle area:', area)

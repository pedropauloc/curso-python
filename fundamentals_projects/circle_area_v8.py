from math import pi


def circle(radius):
    print('Circle area', pi * float(radius) ** 2)


if __name__ == '__main__':
    radius = input('Inform the radius: ')
    circle(radius)

def sum_2(a, b):
    return a + b


def sum_3(a, b, c):
    return a + b + c


def sum_n(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum


if __name__ == '__main__':
    print(sum_2(2, 3))
    print(sum_3(2, 3, 4))
    print(sum_n(2, 3, 4, 5, 6, 7))  # packing


'''
unpacking 
nums = (1, 2, 3) (type tuple)
print(sum_3(*nums))
'''

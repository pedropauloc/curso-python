def get_type_day(day):
    days = {
        (1, 7): 'Weekend',
        tuple(range(2, 7)): 'Weekday',
    }
    chosen_day = (type for numbers, type in days.items() if day in numbers)
    return next(chosen_day, '** Invalid Day **')


if __name__ == '__main__':
    for day in range(0, 9):
        print(f'{day}: {get_type_day(day)}')

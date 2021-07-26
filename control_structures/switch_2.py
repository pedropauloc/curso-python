def get_type_day(day):
    days = {
        1: 'Weekend',
        2: 'Midweek',
        3: 'Midweek',
        4: 'Midweek',
        5: 'Midweek',
        6: 'Midweek',
        7: 'Weekend',

    }
    return days.get(day, ' ** invalid ** ')


if __name__ == '__main__':
    for day in range(9):
        print(f'{day}: {get_type_day(day)}')


'''
def get_days_week(day):
    days = {
        1: 'Sunday',
        2: 'Monday',
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thrusday',
        6: 'Friday',
        7: 'Saturday'
    }
    return days.get(day, ' ** invalid ** ')

if __name__ == '__main__':
    for day in range(0, 9):
        if day in range(2, 6):
            print(f'{day}: {get_days_week(day)}, Weekend')
        elif day == 1 or day == 7:
            print(f'{day}: {get_days_week(day)}, Midweek')

'''

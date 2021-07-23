def age_group(age):
    if 0 <= age < 18:
        return 'Minor'
    if age in range(18, 65): # does not include 65
        return 'Adult'
    if age in range(65, 100):
        return 'Aged'
    if age >= 100:
        return 'Centenary'
    else:
        return 'Invalid age'

if __name__ == '__main__':
    for age in (17, 0, 35, 87, 113, -2):
        print(f'{age}: {age_group(age)}')
# Concepts  Grades
# A         From 10.0 to 9.1
# A-        From 9.0 to 8.1
# B         From 8.0 to 7.1
# B-        From 7.0 to 6.1
# C         From 6.0 to 5.1
# C-        From 5.0 to 4.1
# D         From 4.0 to 3.1
# D-        From 3.0 to 2.1
# E         From 2.0 to 1.1
# E-        From 1.0 to 0.0


# For grades greater than 10 and less than 0, "Invalid Grade" will be impressed.

def valid_grade(grade):
    grade = float(grade)
    if grade >= 9.1:
        return 'A'
    elif grade >= 8.1:
        return 'A-'
    elif grade >= 7.1:
        return 'B'
    elif grade >= 6.1:
        return 'B-'
    elif grade >= 5.1:
        return 'C'
    elif grade >= 4.1:
        return 'C-'
    elif grade >= 3.1:
        return 'D'
    elif grade >= 2.1:
        return 'D-'
    elif grade >= 1.1:
        return 'E'
    elif grade >= 0:
        return 'E-'
    else:
        return 'Invalid grade'


if __name__ == '__main__':
    informed_value = input('Student grade: ')
    concept = valid_grade(informed_value)
    print(concept)

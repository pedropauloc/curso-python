# consumes less memory than a list comprehension
# generates data on demand

generator = (i ** 2 for i in range(1000) if i % 2 == 0)
for number in generator:
    print(number)
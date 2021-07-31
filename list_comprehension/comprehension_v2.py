# [ expression for item in list if conditional ]
double_pairs = [i * 2 for i in range(10) if i % 2 == 0]
print(double_pairs)


# normal version
double_pairs = []
for i in range(10):
    if i % 2 == 0:
        double_pairs.append(i * 2)
print(double_pairs)
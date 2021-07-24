# CONTINUE breaks that loop and goes to the next 
# with the BREAK it leaves the loop
for x in range(1, 11):
    if x % 2 == 0:
        continue
    print(x)

print('========')

for x in range(1, 11):
    if x == 5:
        break
    print(x)

# braks and continue can also be associated with while
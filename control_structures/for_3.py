product = {'name': 'Pen Chic', 'price': 14.99,
           'imported': True, 'Inventory': 793}

# these values are available even outside the for
for key in product:  # . keys 
    print(key)

for value in product.values():
    print(value)

print(key, value)

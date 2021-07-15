its_raining = True

# Search for the one closet to expression [its_raining]
print('Today i have the clothes ' + ('Dry.', 'Wet.')[its_raining])


# Using if
# it is ternary because it has 3 operands -- (1 -'Wet.' if 2 - its_raining else 3 'Dry.')
print('Today i have the clothes ' + ('Wet.' if its_raining else 'Dry.'))
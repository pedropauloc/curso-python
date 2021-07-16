# unlike the lists, the tuple is immutable, you can't change
# Built-in immutable sequence.

tupla = tuple ()
tupla = ()
print(type(tupla))

# tupla = ('one') this way im just creating a string
tupla = ('one', )  
print(tupla[0])

colors = ('Green', 'Yellow', 'Blue', 'White')
print(colors[0])
print(colors[-1])
print(colors[1:])

print(colors.index('Yellow'))
print(colors.count('Blue'))
print(len(colors))
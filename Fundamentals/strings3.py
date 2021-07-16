# strings are immutable
phrase = 'Python is a language great'
print('py' not in phrase)
print('lan' in phrase)

print(len(phrase))
print(phrase.lower())

phrase = phrase.upper()

print(phrase.split()) # Will break the string in spaces
print(phrase.split('A'))
print(phrase.split('E'))

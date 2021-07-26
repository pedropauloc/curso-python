# according to pep8, when defining constants, use capital letters
PROHIBITED_WORDS = {'football', 'religion', 'policy'}

texts = [
    'Joao likes football and policy',
    'The beach was fun'
]

for text in texts:
    # when it finds an intersection, it adds
    inserction = PROHIBITED_WORDS.intersection(set(text.lower().split()))
    if inserction:  # if it's not empty
        print('Text has at least one prohibited word:', inserction)
    else:
        print('Authorized text:', text)

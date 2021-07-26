# according to pep8, when defining constants, use capital letters
PROHIBITED_WORDS = ('football', 'religion', 'policy')

texts = [
    'Joao likes football',
    'The beach was fun'
]

for text in texts:
    for word in text.lower().split():
        if word in PROHIBITED_WORDS:
            print('Text has at least one prohibited word: ', word)
            break
    else:
        print('Authorized text: ', text)

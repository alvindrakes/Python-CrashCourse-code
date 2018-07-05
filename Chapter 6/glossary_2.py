# 6.4 glossary 2.0

# 6.3 Glossary

Glossary = {
    'set' : 'containing unique value',
    'indentation' : 'a line of spaces',
    'key_value_pair' : 'just like structure in C',
    'list' : 'array in C',
    'dictionary' : 'strcuture in C',
    } 

for word, meaning in Glossary.items():
    print('The meaning of the word ' + word + ' is ' + meaning + '.')

Glossary['success'] = 'how to be self discipline'
Glossary['determination'] = 'how to not give up'
Glossary['grit'] = 'how to go through tough times'
Glossary['power'] = 'the ability to control the dynamic'
Glossary['war'] = 'how to fight diligently'


for word, meaning in sorted(Glossary.items()):
    print('The meaning of the word ' + word + ' is ' + meaning + '.')
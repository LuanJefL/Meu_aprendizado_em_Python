import pyperclip

'''Frase_1 = 'Lula1994'

print(Frase_1.endswith('1994'))
print(Frase_1.endswith('Lula1994'))
print(Frase_1.endswith('Lula'))

print(Frase_1.startswith('1994'))
print(Frase_1.startswith('Lula1994'))
print(Frase_1.startswith('Lula')) 

Lista_de_frases = ['Paulo', 'futebool', 'Jojo', str(23)]
frase = ','.join(Lista_de_frases)
print(frase)
frase = frase.split(',')
print(frase)

spam = Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".
Please do not drink it.
Sincerely,
Bob

spam = spam.split('\n')
print(spam)
spam = ' '.join(spam)
print(spam)

spam = 'Dear Alice, How have you been? I am fine. There is a container in the fridge that is labeled "Milk Experiment". Please do not drink it. Sincerely, Bob'
print(('Hello'.ljust(10, '-')) + 'World')
print(spam.rjust((len(spam) + 3), '-'))

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-')) 
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth, '.')) 
    print('\n')
picnicItems = {'sandwiches': 4, 'apples': 12,'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

Letra = '-Casa-sem---teto------'
print(Letra.strip('-'))
print(Letra.rstrip('-'))
print(Letra.lstrip('-'))'''


#Texto para copiar
print(pyperclip.paste())
pyperclip.copy("Isso")


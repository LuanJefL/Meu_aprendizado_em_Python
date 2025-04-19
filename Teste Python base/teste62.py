print('Sede d\'água') #Caractere de escape para ignoras aspas 
print('Sede \nCadê a água') #Para pular uma linha 
print('Água\tPreiso\t Onde estar') #Para tabulação
print('Água \\ Preciso') #Para imprimit uma \
print(r'Água, preiso de d\'água.') #Transforma em uma string pura, ou seja, ignora os caracteres de escape.
print(''' Isso mesmo,
preciso de d'agua''') #Strings de múltiplas linhas, não necessita de caracteres de escape.
'''Isso mesmo que você está pensando,
é uma string é um comentário de múltiplas linhas,
muito útil.'''
Maiúscula = 'IsSO'
Minúsculo = 'iSso'
Maiúscula = Maiúscula.lower()
Minúsculo = Minúsculo.upper()
print(Maiúscula, Minúsculo)
print('ISSO'.isupper())
print('IsSo'.isupper())
print('isso'.islower())
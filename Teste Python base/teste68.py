'''class Teste:
    def __init__(self):
        self.List = []
        self.List.append(Teste().Teste1().elemento1)
    class Teste1:
        def __init__(self):
            self.elemento1 = 2'''
    
        
'''class Teste:
    def __init__(self):
        self.List = []
    class Teste1:
        def __init__(self):
            self.elemento1 = 2

    def update(self):
        self.List.append(Teste().Teste1().elemento1)

Teste_obj = Teste()
Teste_obj.update()
print(Teste_obj.List)'''

'''class Teste:
    def __init__(self):   
        self.x = 460
    def update(self):
        Teste_obj.x -= 5
        return Teste_obj.x

Teste_obj = Teste()

for x in range(0,10):
    print(Teste_obj.update())'''

'''Lista = [0, 1, 2]

Lista.insert(0, Lista[-1])
del Lista[-1]


print(Lista)'''

Lista_de_divisores = []
Número = int(input('Qual número você deseja saber se é primo?'))
for Números_p_dividir in range(0, Número):
    if Número % (Números_p_dividir + 1) == 0:
        Lista_de_divisores.append(Números_p_dividir + 1)
if 1 in Lista_de_divisores and Número in Lista_de_divisores and Número % 2 == 1:
    print(f'O número {Número} é primo') 
    print(Lista_de_divisores)

    
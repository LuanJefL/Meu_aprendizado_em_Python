C1 = 0
C2 = 0
A1 = 0
A2 = 0
def Soma_dos_numeros(Quantidade):
    global C1, C2, A1, A2
    while A1 != Quantidade:
        A1 += 1
        C2 += 1 #gerador de números de 1 em 1
        C1 += C2 #Acumulador, exemplo: 0 = 0 + 1, 1 = 1 + 2, 3 = 3 + 3, 6 = 6 + 4 assim por diante...
    return C1
print(Soma_dos_numeros(3))
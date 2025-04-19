def encontrador_de_duplicadas(Lista):
    Elementos_repitidos = []
    for Quantidade_de_elementos in range(0, len(Lista)):
        Tartaruga = Quantidade_de_elementos
        for Quantidade_de_elementos02 in range(0, len(Lista)):
            Coelho = Quantidade_de_elementos02
            if Tartaruga != Coelho:
                if Lista[Tartaruga] == Lista[Coelho]:
                    if int(Lista[Coelho]) not in Elementos_repitidos:
                        Elementos_repitidos.append(int(Lista[Coelho]))
    return Elementos_repitidos
Lista = []
Quantidade_de_elementos_para_colocar = int(input("Quantidade de número que você deseja colocar:"))
for x in range(0, Quantidade_de_elementos_para_colocar):
    Lista.append(int(input("Número:"))) 
print(Lista)
print(encontrador_de_duplicadas(Lista))
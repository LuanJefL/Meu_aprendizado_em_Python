lista_1 = [input("Digite uma lista com virgulas separando e com and no final da lista ")]
Nova_lista = []
index1 = 0
index2 = 0
index3 = 0
Primeira_parte = 0
Separar_strings_2 = 0
while True:
    if lista_1[0].count(",") + 1 != len(Nova_lista):
        try:
            print(index1, index2)
            index1 = index2 
            index2 = lista_1[0].index(",", 1 + index1,  len(lista_1[0]))
            Nova_lista.append(lista_1[0][index1 + 1: index2])
            print(Nova_lista)
        except:
            print("Carregando...")
    if lista_1[0].count(",") == len(Nova_lista):
        break
while True:
    New_index = lista_1[0].index("and") + 3
    print(New_index)
    New_index2 = lista_1[0].index(",", index2, len(lista_1[0]))
    print(New_index2)
    Nova_lista.append(lista_1[0][New_index2 : New_index - 3])
    Nova_lista.append("and")
    print(Nova_lista)
    Nova_lista.append(lista_1[0][New_index : len(lista_1[0])])
    print(Nova_lista)
    print(Nova_lista) 
    if "and" in Nova_lista:
        break

    
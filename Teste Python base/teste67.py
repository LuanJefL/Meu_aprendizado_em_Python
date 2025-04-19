def Tabela_de_animais(Lista, Quantidade_de_espaço, Caractere):
    Maior_lista = {}
    Max_caracteres = []
    for Quantidade_de_listas in range(0, len(Lista)):
        Maior_lista.setdefault(Quantidade_de_listas + 1, len(Lista[Quantidade_de_listas]))
        for Quantidade_de_elementos in range(0, len(Lista[Quantidade_de_listas])):
            Max_caracteres.append(len(Lista[Quantidade_de_listas][Quantidade_de_elementos]))
    Listas = list(Maior_lista)
    Elementos = list(Maior_lista.values())
    Max_caracteres = max(Max_caracteres)

    for Quantidade_de_listas in range(0, len(Lista)):
        while len(Lista[Quantidade_de_listas]) != max(Elementos):
            Lista[Quantidade_de_listas].append('Não há!')

    #print(Listas)
    #print(Elementos)
    #print(Max_caracteres)
    
    for Número_de_elementos in range(0, max(Elementos)):
        print('')
        for Quantidade_de_listas in range(0, len(Lista)):
                print((Lista[Quantidade_de_listas][Número_de_elementos]).ljust(Max_caracteres + Quantidade_de_espaço, Caractere), end = '')

Tabela = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David', 'Steve'],
['dogs']]

Tabela_de_animais(Tabela, 1, ' ')
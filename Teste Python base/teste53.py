allGuests = {'Alice': {'café': 6, 'apples': 5, 'pretzels': 12},
'Bob': {'ham sandwiches': 3, 'apples': 2},
'Carol': {'cups': 3, 'apple pies': 1}}
def quantidade_de_alimentos(allGuests):
    Alimentos = []
    quantidade_de_alimentos_total = {}
    Quantidade_de_nomes = 0
    Nomes = list(allGuests.keys())
    print(Nomes)
    for Nomes_cada in Nomes:
        Quantidade_de_nomes += 1
        for Alimento in range(0, 1):
            Alimentos.append(list(allGuests[Nomes_cada]))
            for Número_alimentos in range(0, len(allGuests[Nomes_cada])):
                quantidade_de_alimentos_total.setdefault(Alimentos[Quantidade_de_nomes - 1][Número_alimentos], 0)
                quantidade_de_alimentos_total[(Alimentos[Quantidade_de_nomes - 1][Número_alimentos])] += allGuests[Nomes_cada][Alimentos[Quantidade_de_nomes - 1][Número_alimentos]]
                print(Alimentos)
                print(quantidade_de_alimentos_total)        
quantidade_de_alimentos(allGuests)
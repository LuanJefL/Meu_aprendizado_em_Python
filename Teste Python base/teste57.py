inv = {'Total items' : 43, 'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def Espólios(inv, lot):
    Total_items = 0
    for Quantidade_de_loot in range(0, len(lot)):
        inv.setdefault(lot[Quantidade_de_loot], 0)
        inv[lot[Quantidade_de_loot]] += 1
    for items, quantidade in inv.items():
        if 'Total items' not in items:
            print(f'{quantidade} {items}')
            Total_items += quantidade
    inv['Total items'] += Total_items - inv['Total items']
    print(f'Quantidade de items: {inv["Total items"]}')
    return inv
inv = Espólios(inv, dragonLoot)
print(inv)

#Colocar a quantidade total no dicionário... Depois...
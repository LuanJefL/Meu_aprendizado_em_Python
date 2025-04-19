Inventário = {'rope': 1, 'torch': 6, 'gold coin': 42,
'dagger': 1, 'arrow': 12}
def items(Inventário):
    Número_total_de_itens = 0
    for x,v in Inventário.items():
        print(f'{v} {x}')
        Número_total_de_itens += v
    print(f'Número total de itens: {Número_total_de_itens}')
items(Inventário)
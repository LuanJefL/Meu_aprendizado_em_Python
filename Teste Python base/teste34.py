#Achei uma forma mais fácil, passei um dia tentando fazer isso...
Nomes = []
def Centralizador(Quantidade_Selecionada):
    global Quantas_linhas
    for x in range(0, Quantidade_Selecionada):
        Nomes.append(input("Fale os nomes um por um"))
    for Quantidade_de_elementos in range(0, Quantidade_Selecionada):
        print(Nomes[Quantidade_de_elementos].center(Quantas_linhas, '='))
Quantas_linhas = int(input("Quantas linhas você quer?"))
Centralizador(int(input("Quantos nomes você quer colocar?")))

Dicionário = {11 : "o",
    12 : "o",
    13 : "o",
    21 : "o",
    22 : "o",
    23 : "o",
    31 : "o",
    32 : "o",
    33 : "o"}
def verificação(Dicionário):
    for Quantidade_de_casa_v in range(1,4):
        if Dicionário[Quantidade_de_casa_v + 10] == Dicionário[Quantidade_de_casa_v + 20] == Dicionário[Quantidade_de_casa_v + 30] == "x":
            print("Deu certo")
            return True
    for Quantidade_de_casa_h in range(10, 34, 10):
        if Dicionário[Quantidade_de_casa_h + 1] == Dicionário[Quantidade_de_casa_h + 2] == Dicionário[Quantidade_de_casa_h + 3] == "x":
            print("Deu certo")
            return True
    for Quantidade_de_casa_vh in range (0, 3, 2):
        if Dicionário[11 + Quantidade_de_casa_vh] == Dicionário[22] == Dicionário[33 - Quantidade_de_casa_vh] == "x":
            print("Deu certo")
            return True
    return False
print(verificação(Dicionário))

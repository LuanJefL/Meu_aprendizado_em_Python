List = []
A1 = 0
while True:
    A1 += 1
    if A1 != 7:
        catname = input("Nome do gato")
        List.append(catname)
        print(List)
    else:
        break
while True:
    try:
        Exibir = 0
        Exibir = int(input("Qual o gato você que ver?")) - 1
        print(List[Exibir])
    except:
        print("Digite um número inteiro")
    A2 = input("Quer saber o nome de outro?")
    if A2 == "s":
        print("Certo")
    else:
        print("Certo")
        break



    


    


        
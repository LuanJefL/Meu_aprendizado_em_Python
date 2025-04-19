from sys import exit

def jogo_da_velha():
    def Estrutura_jogo_da_velha(Dicionário):
        print("    1     2     3"
            "\n       |     |     " 
           f"\nA   {Dicionário[11]}  |  {Dicionário[12]}  |  {Dicionário[13]}  "
            "\n  _____|_____|_____"
            "\n       |     |     "
           f"\nB   {Dicionário[21]}  |  {Dicionário[22]}  |  {Dicionário[23]}    "
            "\n  _____|_____|_____"
            "\n       |     |     "
           f"\nC   {Dicionário[31]}  |  {Dicionário[32]}  |  {Dicionário[33]}    "
            "\n       |     |     "
            )
    def verificação(Dicionário):
        for Quantidade_de_casa_v in range(1,4):
            if Dicionário[Quantidade_de_casa_v + 10] == Dicionário[Quantidade_de_casa_v + 20] == Dicionário[Quantidade_de_casa_v + 30] == "x" or Dicionário[Quantidade_de_casa_v + 10] == Dicionário[Quantidade_de_casa_v + 20] == Dicionário[Quantidade_de_casa_v + 30] == "o" :
                return True
        for Quantidade_de_casa_h in range(10, 34, 10):
            if Dicionário[Quantidade_de_casa_h + 1] == Dicionário[Quantidade_de_casa_h + 2] == Dicionário[Quantidade_de_casa_h + 3] == "x" or Dicionário[Quantidade_de_casa_h + 1] == Dicionário[Quantidade_de_casa_h + 2] == Dicionário[Quantidade_de_casa_h + 3] == "o":
                return True
        for Quantidade_de_casa_vh in range (0, 3, 2):
            if Dicionário[11 + Quantidade_de_casa_vh] == Dicionário[22] == Dicionário[33 - Quantidade_de_casa_vh] == "x" or Dicionário[11 + Quantidade_de_casa_vh] == Dicionário[22] == Dicionário[33 - Quantidade_de_casa_vh] == "o":
                return True
        return False
    Resposta = input("Quer jogar jogo da velha?\nS/N:")
    Resposta_Conclusão = Resposta == "SIM" or Resposta == "SIm" or Resposta == "Sim" or Resposta == "sim" or Resposta == "S" or Resposta == "s"
    if Resposta_Conclusão == True:
        while True:
            Dicionário = {11 : "-",
            12 : "-",
            13 : "-",
            21 : "-",
            22 : "-",
            23 : "-",
            31 : "-",
            32 : "-",
            33 : "-"}
            Dicionário2 = {"A1": 11,
        "A2": 12,
        "A3": 13,
        "B1": 21,
        "B2": 22,
        "B3": 23,
        "C1": 31,
        "C2": 32,
        "C3": 33}
            Estrutura_jogo_da_velha(Dicionário)
            while True:
                Jogador1 = (input("Jogador 1:\nOnde você vai jogar?")).upper()
                while True:
                    try:
                        if "o" not in Dicionário[Dicionário2[Jogador1]]:
                            if "x" not in Dicionário[Dicionário2[Jogador1]]:
                                Dicionário[Dicionário2[Jogador1]] = "x"
                                break
                        Jogador1 = input("Já há uma marcação nesse lugar\nColoque em outro lugar:").upper()
                    except:
                        print("Digite uma coordenada que tenha no jogo, animal!!!")
                        Jogador1 = input("Digite uma coordenada compatível:").upper()
                Estrutura_jogo_da_velha(Dicionário)   
                if verificação(Dicionário):
                    print("Parabéns jogador 1, você venceu!!!")
                    break
                Jogador2 = (input("Jogador 2:\nOnde você vai jogar?")).upper()
                while True:
                    try:
                        if "x" not in Dicionário[Dicionário2[Jogador2]]:
                            if "o" not in Dicionário[Dicionário2[Jogador2]]:
                                Dicionário[Dicionário2[Jogador2]] = "o"
                                break
                        Jogador2 = input("Já há uma marcação nesse lugar\nColoque em outro lugar:").upper()
                    except:
                        print("Digite uma coordenada que tenha no jogo, animal!!!")
                        Jogador2 = input("Digite uma coordenada compatível:").upper()
                Estrutura_jogo_da_velha(Dicionário)
                if verificação(Dicionário):
                    print("Parabéns jogador 2, você venceu!!!")
                    break
            Resposta_rep = input("Você quer repetir?\nS/N:")
            Resposta_rep_con = Resposta_rep == "SIM" or Resposta_rep == "SIm" or Resposta_rep == "Sim" or Resposta_rep == "sim" or Resposta_rep == "S" or Resposta_rep == "s"
            if Resposta_rep_con != True:
                break 
    else:
        exit()
jogo_da_velha()

#Dá erro quando empata
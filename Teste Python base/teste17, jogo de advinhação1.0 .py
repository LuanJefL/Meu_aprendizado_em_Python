from random import randint
from sys import exit

def Jogo_de_adivinhação():
    print("".center(50, "="),
   "\n" + "Bem-vindos ao jogo de adivinhação".center(50, "="),
   "\n" + "".center(50, "="))
    Resposta = input("\n\n\nVocê quer jogar um jogo?\nS/N:")
    Resposta_Conclusão = Resposta == "SIM" or Resposta == "SIm" or Resposta == "Sim" or Resposta == "sim" or Resposta == "S" or Resposta == "s"
    if Resposta_Conclusão == True:
        while True:
            Número_aleatório = randint(1, 100)
            print("\nQual o número que eu estou pensando?")
            Tentativas = 0
            while True:
                Tentativas += 1
                try:
                    Chute = int(input("\nNúmero"))
                    if Chute > Número_aleatório:
                        print("\nÉ um número menor")
                    elif Chute < Número_aleatório:
                        print("\nÉ um número maior")
                    elif Chute == Número_aleatório:
                        print(f"\nParabéns você acertou com {Tentativas} Tentativas.")
                        break
                except:
                    print("\nDigite um número, não uma palavra.")
            Repetir = input("\nQuer jogar de novo?\nS/N:")
            Repetir_Conclusão = Repetir == "SIM" or Repetir == "SIm" or Repetir == "Sim" or Repetir == "sim" or Repetir == "S" or Repetir == "s"
            if Repetir_Conclusão != True:
                break          
    else:
        exit()
Jogo_de_adivinhação()
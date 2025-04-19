#list = ["EAI"]
#print(sum(list))
#3print("EAI" in list)
import sys
Lista = []
def Adicionar_nomes(Quantidade):
    global Lista
    for x in range(0, Quantidade):
        Lista.append(input("Digite os nomes de forma solo"))
        print(Lista)
        if x == (Quantidade - 1):
            break
        Confirmação_para_continuar = input("Quer adicionar outro nome?")
        Respostas = Confirmação_para_continuar == "SIM" or Confirmação_para_continuar == "SIm" or Confirmação_para_continuar == "Sim" or Confirmação_para_continuar == "sim" or Confirmação_para_continuar == "S" or Confirmação_para_continuar == "s"  
        if Respostas != True:
            break
    return Lista
Confirmação_para_continuar = input("Quer adicionar nomes?")
Respostas = Confirmação_para_continuar == "SIM" or Confirmação_para_continuar == "SIm" or Confirmação_para_continuar == "Sim" or Confirmação_para_continuar == "sim" or Confirmação_para_continuar == "S" or Confirmação_para_continuar == "s"
if Respostas == True:
    Quantidade = int(input("Qual a Quantidade de nomes você vai querer?"))
    Adicionar_nomes(Quantidade)
else:
    sys.exit()
print(Lista)
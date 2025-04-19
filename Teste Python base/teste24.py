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
Lista_05 = Lista
def Centralizador(Lista):
    global Lista_05
    Traços = "="
    Quantidade_de_Números = 0
    Lista_0 = Lista_05
    Números_de_elementos = len(Lista_0) # len = 3
    for Contador_de_quantidade in range(0, Números_de_elementos): 
        Quantidade_de_Números += len(Lista_0[Contador_de_quantidade]) 
        if Quantidade_de_Números % 2 == 0:
            Quantidade_de_Números += 1   
    for Contador_de_quantidade in range(0, Números_de_elementos):
        Strings_de_cada_lista = len(Lista_0[Contador_de_quantidade])
        Quantidade_divido_1 = int((Quantidade_de_Números - Strings_de_cada_lista) / 2)
        Quantidade_divido_2 = Quantidade_divido_1
        if Strings_de_cada_lista % 2 == 1:
            Quantidade_divido_2 -= 1
        Palavras = (Traços * (Quantidade_de_Números - (Strings_de_cada_lista + Quantidade_divido_1))) + (Lista_0[Contador_de_quantidade]) + (Traços * (Quantidade_de_Números - (Strings_de_cada_lista + Quantidade_divido_2)))
        print(Palavras)
Centralizador(Lista_05)
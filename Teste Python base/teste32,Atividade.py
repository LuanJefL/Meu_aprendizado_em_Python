import sys

Lista = []
Nova_lista = []
Local_das_Vírgulas_1 = 0

Resposta = input("Quer adicionar itens? s/n")
Resposta_Conclusão = Resposta == "SIM" or Resposta == "SIm" or Resposta == "Sim" or Resposta == "sim" or Resposta == "S" or Resposta == "s"
if Resposta_Conclusão == True:
    print("Digite uma lista com vírgulas e and depois do penúltimo item")
    print("Exemplo: Fulano, Cicrano, Sujeito and Pessoa")
    Lista.append(input("Digite:"))
else:
    sys.exit()

def Separador(Lista):
    global Nova_lista, Local_das_Vírgulas_1 
    Correção_para_continuar = 0
    try:
       if Lista[0].count(",") == 1:
           Correção_para_continuar = 1
       for Quantidade_de_vírgulas in range(0, (Lista[0].count(",") - 1) + (Correção_para_continuar)):
            try:
                if Local_das_Vírgulas_1 == 0:
                    Local_das_Vírgulas_2 = Lista[0].index(",", Local_das_Vírgulas_1)
                    Nova_lista.append(Lista[0][Local_das_Vírgulas_1 : (Local_das_Vírgulas_2)])
                try:
                    Local_das_Vírgulas_1 = Local_das_Vírgulas_2
                    Local_das_Vírgulas_2 = Lista[0].index(",", (Local_das_Vírgulas_1 + 1))
                    Nova_lista.append(Lista[0][(Local_das_Vírgulas_1 + 2) : Local_das_Vírgulas_2])
                    print(Nova_lista)
                except:
                    print("Carregando...")
                    break
            except:
                print("Alguma coisa deu errado")
                break
    except:
        print("Carrengado...")
    for Quantidade_de_and in range(0, Lista[0].count("and")):
        Local_do_and = Lista[0].index("and")
        try:
            Nova_lista.append(Lista[0][Local_das_Vírgulas_2 + 2: Local_do_and - 1])
        except:
            Nova_lista.append(Lista[0][Local_das_Vírgulas_1 : (Local_do_and - 1)])
        Nova_lista.append(Lista[0][Local_do_and + 4:])
        print("Deu Certo")
        return(Nova_lista)

Lista_organizada = Separador(Lista)
print(Lista_organizada)
for Quantidade_de_elementos in range(0, len(Lista_organizada)):
    print(Lista_organizada[Quantidade_de_elementos])
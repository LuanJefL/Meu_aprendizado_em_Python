import time
import random
import math

Velócidade = 10
Ações_p_seg = 30
Movimento_fx = 0
x = 10
y = 0
x2 = 0
Cópia_x = 0
y2 = 0
Cópia_y = 0
Velócidade_x = 10
Fps = 60
Confirmação_mov = 0

#Transição lisa
Lista_fluída = []
Lista_reposição_x = []
Lista_reposição_y = []
Contador_fluídez = 0


Lista_posição = []
Tamanho_da_Cobra = 3

def Corpo():
    
    while len(Lista_posição) > Tamanho_da_Cobra:
        del Lista_posição[0]
    return Lista_posição

#Lisa
def Corpo_liso():
    while len(Lista_fluída) > Tamanho_da_Cobra:
        del Lista_fluída[0]
    return Lista_fluída
    


while True:

    Fluidez = Velócidade / math.ceil(Fps / Ações_p_seg)
 
    

    if x - Cópia_x == Velócidade:
        x2 += Fluidez
    if x - Cópia_x == Velócidade * -1:
        x2 -= Fluidez
    if y - Cópia_y == Velócidade:
        y2 += Fluidez
    if y - Cópia_y == Velócidade * -1:
        y2 -= Fluidez

    
    
    if x >= 460:
        break
    if x <= 0:
        break

    #Lisa
    Lista_reposição_x.append(x2)
    Lista_reposição_y.append(y2)
    Movimento_fluído = Corpo_liso()

    #print(Movimento_fluído, x)


    #Lisa
    for quantidade_listas in range(0, len(Movimento_fluído)):
        for quantidade_de_lista_2 in range(0, len(Movimento_fluído[0][0])):
                print(Movimento_fluído[quantidade_listas][0][quantidade_de_lista_2][Contador_fluídez])
                print(Movimento_fluído[quantidade_listas][1][quantidade_de_lista_2][Contador_fluídez])
    Contador_fluídez += 1
    if Contador_fluídez == math.ceil(Fps / Ações_p_seg):
        Contador_fluídez = 0

        
    if Confirmação_mov <= Fps:
            Confirmação_mov += Ações_p_seg
    if Confirmação_mov >= Fps:

        

        Cópia_y = y
        y2 = Cópia_y

        Cópia_x = x
        x2 = Cópia_x

        print(Movimento_fluído)

        #Lisa
        Lista_fluída.append([[Lista_reposição_x], [Lista_reposição_y]])
        Lista_reposição_x = []
        Lista_reposição_y = []


        Lista_posição.append((x, y))

        

        x += Velócidade_x
        y += Velócidade_x

        
        
    if Confirmação_mov >= Fps:
            Confirmação_mov = 0   
    
    Comprimento = Corpo()

    #print(Comprimento, x)

    for Quantidade_de_elementos in range(0, len(Comprimento)):
        pass
        #print(Comprimento[Quantidade_de_elementos][0], Comprimento[Quantidade_de_elementos][1], x)

    for Quantidade_de_Cabeças in range(0, len(Comprimento)):
        x == Comprimento[Quantidade_de_Cabeças][0], Comprimento[Quantidade_de_Cabeças][0], x

    



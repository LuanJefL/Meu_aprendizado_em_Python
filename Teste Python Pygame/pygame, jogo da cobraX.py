import pygame
import math
import random

pygame.init()
Largura = 460
Altura = 460
Tela = pygame.display.set_mode((Largura, Altura))
pygame.display.set_caption('Programa')
Camada = pygame.Surface((Largura, Altura), pygame.SRCALPHA)
Camada01 = pygame.Surface((Largura, Altura), pygame.SRCALPHA)
Running = True
Relógio = pygame.time.Clock()

#Config
Fps = 60
Tamanho = 20
Velócidade = Tamanho
Confirmação_mov = 0
Ações_p_seg = 6

#Posições iniciais
Velócidade_y = Velócidade
Velócidade_x = 0
Evitar_colisãoy = True
Evitar_colisãox = True

x = 240
x2 = -20
Cópia_x = 0
y = 240
y2 = -20
Cópia_y = 0

Lugar_aleatório_x = 20
Lugar_aleatório_y = 20

Lista_posição = [(240, y - (Tamanho * 3)), (240, y - (Tamanho * 2)), (240, y - Tamanho)]
Tamanho_da_Cobra = 3

#Transição lisa
Lista_fluída = []
Lista_reposição_x = []
Lista_reposição_y = []
Contador_fluídez = 0

#Estado
Morte = False

#Cores
Verde_Escuro = (0, 175, 0)

#Fonte e messagem
Fonte = pygame.font.SysFont('Arial', 25, True, False)
Messagem_Morte_f = Fonte.render('Você morreu.', False, 'Black')
Messagem_Morte_f_Meio = Messagem_Morte_f.get_rect()
Messagem_Morte_f_Meio.center = (Largura / 2, Altura / 2)
Messagem_p_jogar_dnv_f = Fonte.render('Aperte SPACE para recomeçar', False, 'Black')
Messagem_p_jogar_dnv_f_Meio = Messagem_p_jogar_dnv_f.get_rect()
Messagem_p_jogar_dnv_f_Meio.center = (Largura / 2, (Altura / 2) + 25)



def Cobra(x, y):
    Triângulo = pygame.draw.rect(Camada, 'Blue', (x, y, Tamanho, Tamanho), 0) #(x, y, Largura em pixels, altura em pixels) para centralizar basta dividir a largura e o tamanho por dois e subtrair as coordenadas que foram divididas por dois
    return Triângulo

def Corpo_liso():
    while len(Lista_fluída) > Tamanho_da_Cobra:
        del Lista_fluída[0]
    return Lista_fluída

def Xadrez(Largura, Altura, Tamanho, Cor):
    Posição_x = Tamanho * -1
    Mudança = Tamanho
    Variando = Tamanho
    Posição_y = 0
    for Quantidade_de_casas1 in range(0, int(Largura / Tamanho)):
        Mudança = Mudança * -1
        Variando += Mudança
        Posição_y = Variando
        Posição_x += Tamanho
            
        for Quantidade_de_casash in range(0, int(math.ceil((Altura / Tamanho) / 2))):
            Retángulo = pygame.draw.rect(Camada, Cor, (Posição_x, Posição_y, Tamanho, Tamanho), 0)
            Posição_y += Tamanho * 2

def Corpo(Lista_Posição):
    while len(Lista_posição) > Tamanho_da_Cobra:
        del Lista_posição[0]
    return Lista_posição

def Fruta(Lugar_aleatório_x, Lugar_aleatório_y, Tamanho):
    Fru = pygame.draw.rect(Camada, 'red', (Lugar_aleatório_x, Lugar_aleatório_y, Tamanho, Tamanho), 0)
    return Fru

def Reiniciar():
    global Velócidade_y, Velócidade_x, Evitar_colisãoy, Evitar_colisãox, x, x2, Cópia_x, y, y2, Cópia_y, Lugar_aleatório_x, Lugar_aleatório_y, Lista_posição, Tamanho_da_Cobra, Morte
    Velócidade_y = Velócidade
    Velócidade_x = 0
    Evitar_colisãoy = True
    Evitar_colisãox = True
    x = 240
    x2 = 0
    Cópia_x = 0
    y = 240
    y2 = 0
    Cópia_y = 0
    Lugar_aleatório_x = 20
    Lugar_aleatório_y = 20
    Lista_posição = [(240, 220), (240, 200), (240, 180)]
    Tamanho_da_Cobra = 3
    Morte = False


def input():
    global Velócidade_x, Velócidade_y, Evitar_colisãoy, Evitar_colisãox
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and Evitar_colisãox:
        Velócidade_x = Velócidade - (Velócidade + Velócidade)
        Velócidade_y = 0
        Evitar_colisãox = False
        Evitar_colisãoy = True
    if keys[pygame.K_d] and Evitar_colisãox:
        Velócidade_x = Velócidade
        Velócidade_y = 0
        Evitar_colisãox = False
        Evitar_colisãoy = True
    if keys[pygame.K_s] and Evitar_colisãoy:
        Velócidade_y = Velócidade
        Velócidade_x = 0
        Evitar_colisãox = True
        Evitar_colisãoy = False
    if keys[pygame.K_w] and Evitar_colisãoy:
        Velócidade_y = Velócidade - (Velócidade + Velócidade)
        Velócidade_x = 0
        Evitar_colisãox = True
        Evitar_colisãoy = False
    #Tem um bug que faz a cobra voltar a direção ccontrária quando se aperta os botões muito rápido 
            

def Movimentação():
    global x, y
    x += Velócidade_x
    y += Velócidade_y  


def Movimento():
    global Confirmação_mov, Fps, Ações_p_seg, Cópia_x, x2, x, y, y2, Cópia_y, Running, Morte, Lista_reposição_x, Lista_reposição_y
    if Confirmação_mov <= Fps:
        Confirmação_mov += Ações_p_seg
    if Confirmação_mov >= Fps:

        Cópia_x = x
        x2 = Cópia_x

        Cópia_y = y
        y2 = Cópia_y


        Lista_fluída.append([[Lista_reposição_x], [Lista_reposição_y]])
        Lista_reposição_x = []
        Lista_reposição_y = []

        Lista_posição.append((x, y))


        Movimentação()

        
        if y <= Altura - (Altura + Tamanho):
            y = Altura - Tamanho
        if y >= Altura:
            y = Altura - Altura
        if x <= Largura - (Largura + Tamanho):
            x = Largura - Tamanho
        if x >= Largura:
            x = Largura - Largura
            

        if Comprimento.count((x, y)) >= 1:
            Morte = True
            Segundos = 0
            Alpha = 0
            while Morte:
                Segundos += Relógio.get_time() / 1000
                Messagem_Morte_f.set_alpha(int(Segundos * 10))
                Messagem_p_jogar_dnv_f.set_alpha(int(Segundos * 10))
                Tela.blit(Camada01, (0, 0))
                Camada01.fill((255, 255, 255, 1))
                Camada01.blit(Messagem_Morte_f, Messagem_Morte_f_Meio)
                Camada01.blit(Messagem_p_jogar_dnv_f, Messagem_p_jogar_dnv_f_Meio)
                keys = pygame.key.get_pressed()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Running = False
                        Morte = False
                if keys[pygame.K_SPACE]:
                    Reiniciar()
                pygame.display.update()
                
        

    if Confirmação_mov >= Fps:
        Confirmação_mov = 0  
      


while Running:
    Relógio.tick(Fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    Tela.fill('white')
    Tela.blit(Camada, (0,0))
    Camada.fill(('green'))
    Xadrez(Largura, Altura, Tamanho, Verde_Escuro)

    Fruta(Lugar_aleatório_x, Lugar_aleatório_y, Tamanho)
    
    
    
    
    input()
    
     
     
        
    Fluidez = Velócidade / math.ceil(Fps / Ações_p_seg)
    
    if x - Cópia_x == Velócidade:
        x2 += Fluidez
        
    if x - Cópia_x == Velócidade * -1:
        x2 -= Fluidez

    if y - Cópia_y == Velócidade:
        y2 += Fluidez
        
    if y - Cópia_y == Velócidade * -1:
        y2 -= Fluidez


    #Lisa
    Lista_reposição_x.append(x2)
    Lista_reposição_y.append(y2)
    Movimento_fluído = Corpo_liso()

    for quantidade_listas in range(0, len(Movimento_fluído)):
        for quantidade_de_lista_2 in range(0, len(Movimento_fluído[0][0])):
                Cobra(Movimento_fluído[quantidade_listas][0][quantidade_de_lista_2][Contador_fluídez], Movimento_fluído[quantidade_listas][1][quantidade_de_lista_2][Contador_fluídez])
    
    Contador_fluídez += 1
    if Contador_fluídez == math.ceil(Fps / Ações_p_seg):
        Contador_fluídez = 0
    

    Cobra(x2, y2)

    


    Comprimento = Corpo(Lista_posição)

    #print(x, y, Lista_posição)

    for Quantidade_de_elementos in range(0, len(Comprimento)):
            #pass
            Cobra(Comprimento[Quantidade_de_elementos][0], Lista_posição[Quantidade_de_elementos][1])
    

    if (x, y) == (Lugar_aleatório_x, Lugar_aleatório_y):
        Lugares_Xey = (Largura - Tamanho) / Tamanho
        
        Local_x = random.randint(0, Lugares_Xey)
        Lugar_aleatório_x = Local_x * Tamanho

        Local_y = random.randint(0, Lugares_Xey)
        Lugar_aleatório_y = Local_y * Tamanho

        Tamanho_da_Cobra += 1

    
    Movimento()
    pygame.display.update()
pygame.quit()


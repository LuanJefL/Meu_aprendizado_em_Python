import pygame

pygame.init()
Largura = 460
Altura = 460
Tela = pygame.display.set_mode((Largura, Altura))
Camada = pygame.Surface((Largura, Altura), pygame.SRCALPHA)
pygame.display.set_caption('Teste')
Relógio = pygame.time.Clock()
Run = True
Fps = 60


x = 0
y = 0

#Hit box
Largura_h = 20
Altura_h = 30

#Física
gravity = True
Colisão = True
Exibir_Hit_Box = True
Aceleração_f = 0
Tamanho_do_pulo = -5
Velocidade = 5



def Chão(Posição_x, Posição_y, Largura, Altura):
    global Relógio, Aceleração_f, y, Keys
    Chão_h = (Posição_x, Posição_y, Largura, Altura)

    if Exibir_Hit_Box:
        Forma = pygame.draw.rect(Camada, 'white', Chão_h, 1)


    if (Posição_x - Largura_h) < x < (Posição_x + Largura) and (Posição_y - Altura_h) < y < (Posição_y + Altura):
        if Colisão:
            Aceleração_f = 0
            y = Posição_y - Altura_h
            Relógio = pygame.time.Clock()
            if Keys[pygame.K_SPACE]:
                 Aceleração_f = Tamanho_do_pulo

def Plataforma(Posição_x, Posição_y, Largura, Altura): #40, 5
    global Aceleração_f, Relógio, y, Keys
    Plat_h = (Posição_x, Posição_y, Largura, (Altura / 2))
    Teto_h = (Posição_x, Posição_y + (Altura / 2), Largura, (Altura / 2))

    if Exibir_Hit_Box:
        Plat = pygame.draw.rect(Camada, (255,255,255), Plat_h, 1)
        Teto = pygame.draw.rect(Camada, (0,0,255), Teto_h, 1)

    if (Posição_x - Largura_h) < x < (Posição_x + Largura) and (Posição_y - Altura_h) < y < (Posição_y + (Altura / 2)):
        if Colisão:
            Aceleração_f = 0
            y = Posição_y - Altura_h
            Relógio = pygame.time.Clock()
            if Keys[pygame.K_SPACE]:
                Aceleração_f = Tamanho_do_pulo


    if (Posição_x - Largura_h) < x < (Posição_x + Largura) and ((Posição_y + (Altura / 2)) - Altura_h) < y < ((Posição_y + (Altura / 2)) + (Altura / 2)):
        if Colisão:
            Aceleração_f = 0
            Relógio = pygame.time.Clock()

    
def Parede_Escalavel(Posição_x, Posição_y, Largura, Altura):
    global x, y, Relógio, Aceleração_f, Keys
    Tamanho_do_chão_porcentagem = 3
    
    Parede_E_h = (Posição_x, (Posição_y + (Altura / Tamanho_do_chão_porcentagem)), (Largura / 2), (Altura - (Altura / Tamanho_do_chão_porcentagem)))
    Parede_D_h = (Posição_x + (Largura / 2), (Posição_y + (Altura / Tamanho_do_chão_porcentagem)), (Largura / 2), (Altura - (Altura / Tamanho_do_chão_porcentagem)))
    Chão_h = (Posição_x, Posição_y, Largura, (Altura / Tamanho_do_chão_porcentagem))
    
    if Exibir_Hit_Box:
        Parede_E = pygame.draw.rect(Camada, 'white', Parede_E_h, 1) # 10, 100 no total
        Parede_D = pygame.draw.rect(Camada, 'white', Parede_D_h, 1)
        Chão = pygame.draw.rect(Camada, 'white', Chão_h, 1)

    if (Posição_x - Largura_h) < x < (Posição_x + (Largura / 2)) and ((Posição_y + (Altura / Tamanho_do_chão_porcentagem)) - Altura_h) < y < ((Posição_y + (Altura / Tamanho_do_chão_porcentagem)) + (Altura - (Altura / Tamanho_do_chão_porcentagem))):
        if Colisão:
            x = Posição_x - Largura_h
            Relógio = pygame.time.Clock()

    if ((Posição_x + (Largura / 2)) - Largura_h) < x < ((Posição_x + (Largura / 2)) + (Largura / 2)) and ((Posição_y + (Altura / Tamanho_do_chão_porcentagem)) - Altura_h) < y < ((Posição_y + (Altura / Tamanho_do_chão_porcentagem)) + (Altura - (Altura / Tamanho_do_chão_porcentagem))):
        if Colisão:
            x = Posição_x + Largura
            Relógio = pygame.time.Clock()

    if (Posição_x - Largura_h) < x < (Posição_x + Largura) and (Posição_y - Altura_h) < y < (Posição_y + (Altura / Tamanho_do_chão_porcentagem)):
        if Colisão:
            Aceleração_f = 0
            y = Posição_y - Altura_h 
            Relógio = pygame.time.Clock()
            if Keys[pygame.K_SPACE]:
                Aceleração_f = Tamanho_do_pulo





def Hit_box(x, y, Cor):
    if Exibir_Hit_Box:
        Figura = pygame.draw.rect(Camada, Cor, (x, y, Largura_h, Altura_h), 1)

def Personagem(x, y, Cor):
    Figura = pygame.draw.rect(Camada, Cor, (x, y, 20, 30), 0)
    



def Gravidade():
    G = 9.807
    T = Relógio.get_time() / 1000
    F = G * T
    return F


while Run:
    Relógio.tick(Fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False
    
    Tela.fill('orange')
    Tela.blit(Camada, (0,0))
    Camada.fill('orange')

    

    Keys = pygame.key.get_pressed()
    if Keys[pygame.K_a]:
        x -= Velocidade
    if Keys[pygame.K_d]:
        x += Velocidade
    
    if Keys[pygame.K_LSHIFT]:
        Altura_h = 15
        y += 15
    if not Keys[pygame.K_LSHIFT]:
        Altura_h = 30
    if not gravity:
        if Keys[pygame.K_w]:
            y -= Velocidade
        if Keys[pygame.K_s]:
            y += Velocidade
    

    if gravity:
        Aceleração_f += Gravidade()
        y += Aceleração_f

    
    Chão(0, 440, 460, 20)
    Plataforma(20, 400, 40, 10)
    Parede_Escalavel(390, 20, 50, 400)
    Hit_box(x, y, 'black')
    Personagem(x, y, 'white')


    if x <= -20:
        x = 440
    if x >= 460:
        x = 0


    pygame.display.update()
pygame.quit()

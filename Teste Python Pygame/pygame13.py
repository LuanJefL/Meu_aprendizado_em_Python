import pygame

pygame.init()
pygame.mixer.music.set_volume(0.9)#Valores de 0 a 1
Música_de_fundo = pygame.mixer.music.load('C:\Minhas coisas\Vs code\Testes Python\Teste Python Pygame\Trilha sonora, pygame13.mp3')
#pygame.mixer.music.play(-1)
Barulho_pulo = pygame.mixer.Sound('C:\Minhas coisas\Vs code\Testes Python\Teste Python Pygame\Efeito-Sonoro-MOLA-_toim-oim-oim_.wav')
Barulho_pulo.set_volume(0.3)#Valores de 0 a 1
Largura = 460
Altura = 460
Tela = pygame.display.set_mode((Largura, Altura))
pygame.display.set_caption('Teste')
Camada = pygame.Surface((Largura, Altura), pygame.SRCALPHA)
Relógio = pygame.time.Clock()
Running = True
Fps = 60
Velócidade = 5

#Hit box
Largura_h = 20
Altura_h = 30


x = 0
y = 0



#Física
Aceleração_f = 0
Tamanho_do_pulo = -5

def Chão(Posição_x, Posição_y, Largura, Altura, Personagem):
    global y, Keys, Aceleração_f, Relógio
    chão = pygame.draw.rect(Tela, (255,255,255), (Posição_x, Posição_y, Largura, Altura), 0)

    #Forma_Super = pygame.Surface(pygame.Rect((Posição_x, Posição_y, Largura, Altura)).size, pygame.SRCALPHA)
    #pygame.draw.rect(Forma_Super, 'white', Forma_Super.get_rect())
    #Camada.blit(Forma_Super, (Posição_x, Posição_y, Largura, Altura))

    if Personagem.colliderect(chão):
        Aceleração_f = 0
        y = Posição_y - Altura_h
        Relógio = pygame.time.Clock()

    if Keys[pygame.K_SPACE] and Personagem.colliderect(chão):
        Aceleração_f = Tamanho_do_pulo
        #Barulho_pulo.play()
    
    return chão

def Plataforma(Posição_x, Posição_y, Largura, Altura, Personagem): #40, 5
    global Aceleração_f, Relógio, y, Keys
    Plat = pygame.draw.rect(Tela, (0,0,0,0), (Posição_x, Posição_y, Largura, (Altura / 2)), 0)
    Teto = pygame.draw.rect(Tela, (0,0,0,0), (Posição_x, Posição_y + (Altura / 2), Largura, (Altura / 2)), 0)
    
    Forma_Super = pygame.Surface(pygame.Rect((Posição_x, Posição_y, Largura, Altura)).size, pygame.SRCALPHA)
    pygame.draw.rect(Forma_Super, 'black', Forma_Super.get_rect())
    Camada.blit(Forma_Super, (Posição_x, Posição_y, Largura, Altura))

    if Personagem.colliderect(Plat):
        Aceleração_f = 0
        y = Posição_y - 30
        #371
        Relógio = pygame.time.Clock()

    if Personagem.colliderect(Teto):
        Aceleração_f = 0
        Relógio = pygame.time.Clock()

    if Keys[pygame.K_SPACE] and Personagem.colliderect(Plat):
        Aceleração_f = Tamanho_do_pulo




def Parede_Escalavel(Posição_x, Posição_y, Largura, Altura, Personagem):
    global x, y, Relógio, Aceleração_f, Keys
    Tamanho_do_chão_porcentagem = 10
    
    Parede_E = pygame.draw.rect(Camada, 'white', (Posição_x, (Posição_y + (Altura / Tamanho_do_chão_porcentagem)), (Largura / 2), (Altura - (Altura / Tamanho_do_chão_porcentagem))), 0) # 10, 100 no total
    Parede_D = pygame.draw.rect(Camada, 'white', (Posição_x + (Largura / 2), (Posição_y + (Altura / Tamanho_do_chão_porcentagem)), (Largura / 2), (Altura - (Altura / Tamanho_do_chão_porcentagem))), 0)
    Chão = pygame.draw.rect(Camada, 'white', (Posição_x, Posição_y, Largura, (Altura / Tamanho_do_chão_porcentagem)), 0)

    if Personagem.colliderect(Parede_E): #390, 350
        x = Posição_x - Largura_h
        Relógio = pygame.time.Clock()

    if Personagem.colliderect(Parede_D):
        x = Posição_x + Largura
        Relógio = pygame.time.Clock()

    if Personagem.colliderect(Chão):
        Aceleração_f = 0
        y = Posição_y - Altura_h 
        #371
        Relógio = pygame.time.Clock()

    if Keys[pygame.K_SPACE] and Personagem.colliderect(Chão):
        Aceleração_f = Tamanho_do_pulo
    
    return Parede_E, Parede_D, Chão

def Hit_box(x, y, Cor):
    Largura = Largura_h
    Altura = Altura_h
    Figura = pygame.draw.rect(Tela, Cor, (x, y, Largura, Altura))
    return Figura

def Personagem(Superficíe, Cor, Rect):
    Forma_Super = pygame.Surface(pygame.Rect(Rect).size, pygame.SRCALPHA)
    pygame.draw.rect(Forma_Super, Cor, Forma_Super.get_rect())
    Superficíe.blit(Forma_Super, Rect)


def Gravidade():
    G = 9.807
    T = Relógio.get_time() / 1000
    F = G * T
    return F



while Running:
    Relógio.tick(Fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    Tela.fill('Orange')
    Tela.blit(Camada, (0, 0))
    Camada.fill('Orange')
    
    
    
    
    

    Keys = pygame.key.get_pressed()
    if Keys[pygame.K_a]:
        x -= Velócidade
    if Keys[pygame.K_d]:
        x += Velócidade
    if Keys[pygame.K_LSHIFT]:
        y = 0
        x = 0
        Aceleração_f = 0
    
    

        

    
    Aceleração_f += Gravidade()
    
    y += Aceleração_f
    C = 0

    Hit_box(x, y, (0,0,255,C))
    Chão(0, 440, 460, 20, Hit_box(x, y, (0,0,255,C)))
    Plataforma(20, 300, 40, 10, Hit_box(x, y, (0,0,0,C)))
    Plataforma(20, 400, 40, 10, Hit_box(x, y, (0,0,0,C)))
    

    
    
    
    #Plataforma(30, 200, 40, 10, Hit_box(x, y, (0,0,0,C)))
    #Plataforma(315, 239, 40, 10, Hit_box(x, y, (0,0,0,C)))
    #Parede_Escalavel(20, 110, 10, 100, Hit_box(x, y, (0,0,0,C)))
    #Parede_Escalavel(390, 350, 10, 100, Hit_box(x, y, (0,0,0,C)))
    
    Personagem(Tela, (0,0,255), (x, y + 5, Largura_h, Altura_h - 5))

    if x <= -20:
        x = 440
    if x >= 460:
        x = 0

    pygame.display.update()
pygame.quit()
import pygame

pygame.init()
Largura = 460
Altura = 460
Tela = pygame.display.set_mode((Largura, Altura))
pygame.display.set_caption('Teste')
Relógio = pygame.time.Clock()
Running = True
Fps = 60
Velócidade = 5
Fonte = pygame.font.SysFont('Arial', 20, True, False)

Aceleração_f = 0

def Chão():
   chão = pygame.draw.rect(Tela, 'white', (0, 440, 460, 20), 0)
   return chão

def Personagem(x, y):
    Figura = pygame.draw.rect(Tela, 'Black', (x, y, 20, 30))
    return Figura
x = 0
y = 0

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
    Chão()
    Personagem(x, y)
    Coordenadas_T = f'X:{x}, Y: {int(y)}'
    Coordenada_F = Fonte.render(Coordenadas_T, False, 'black') 

    
    

    Keys = pygame.key.get_pressed()
    if Keys[pygame.K_a]:
        x -= Velócidade
    if Keys[pygame.K_d]:
        x += Velócidade
    if Keys[pygame.K_LSHIFT]:
        y = 0
        x = 0
        Aceleração_f = 0
    if Keys[pygame.K_SPACE] and Personagem(x, y).colliderect(Chão()):
        Aceleração_f = -5
    

        
    
    
    Aceleração_f += Gravidade()
    
    
    
    y += Aceleração_f
    
    if Personagem(x, y).colliderect(Chão()):
        Aceleração_f = 0
        y = 411
        Relógio = pygame.time.Clock()
    

    if x <= -20:
        x = 440
    if x >= 460:
        x = 0

    
    Tela.blit(Coordenada_F, (0, 0))
    pygame.display.update()
pygame.quit
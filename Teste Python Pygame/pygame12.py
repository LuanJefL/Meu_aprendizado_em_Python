import pygame

pygame.init()
Largura = 460
Altura = 460
Tela = pygame.display.set_mode((Largura, Altura))
pygame.display.set_caption('Teste')
Relógio = pygame.time.Clock()
Running = True
Fps = 60

Velocidade_d_queda = 0
Gravidade = 9
Tempo = 0
Segundos = 0
Força_do_pulo = 9
Tamanho_do_pulo = 0

def Chão():
   chão = pygame.draw.rect(Tela, 'white', (0, 440, 460, 20), 0)
   return chão

def Personagem(x, y):
    Figura = pygame.draw.rect(Tela, 'Black', (x, y, 20, 30))
    return Figura
x = 0
y = 0

while Running:
    Relógio.tick(Fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    Tela.fill('Orange')
    Chão()
    Personagem(x, y)

    
    

    Keys = pygame.key.get_pressed()
    if Keys[pygame.K_a]:
        x -= 3
    if Keys[pygame.K_d]:
        x += 3
    if Keys[pygame.K_LSHIFT]:
        y = 0
    if Keys[pygame.K_SPACE] and Personagem(x, y).colliderect(Chão()) or Força_do_pulo != 9:
        Força_do_pulo -= 1
        Tamanho_do_pulo += Força_do_pulo * Gravidade
        print(Tamanho_do_pulo)
        y -= Tamanho_do_pulo
        if Força_do_pulo == 0:
            Força_do_pulo = 9
            Tamanho_do_pulo = 0

    if Personagem(x, y).colliderect(Chão()):
        Segundos = 0
        Velocidade_d_queda = 0
        y = 410
    if not Personagem(x, y).colliderect(Chão()):
        y += Velocidade_d_queda
        Tempo += 60 / Fps
        if Tempo == 6:
            Segundos += 0.1
            Tempo = 0
        Velocidade_d_queda = Gravidade * Segundos 
    

    
    pygame.display.update()
pygame.quit
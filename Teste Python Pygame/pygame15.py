import pygame

pygame.init()
Largura = 460
Altura = 460
Tela = pygame.display.set_mode((Largura, Altura))
pygame.display.set_caption('Teste')
Camada = pygame.Surface((Largura, Altura), pygame.SRCALPHA)
Relógio = pygame.time.Clock()
Running = True
Fps = 60
Fonte = pygame.font.SysFont('Arial', 20, True, False) #Fonte, Tamanho, Negrito e italico

while Running:
    Relógio.tick(Fps)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            Running = False
    Tela.fill('Orange')
    Tela.blit(Camada, (0, 0))
    Camada.fill('Orange')
    Messagem = "Você consegue"
    Messagem_F = Fonte.render(Messagem, True, (0, 0, 0) ) #Messagem, Antiserrilos e cor
    Messagem_F.set_alpha(0) # Transparência 

    Camada.blit(Messagem_F, (0, 0)) #Texto formatado e coordenadas.
    pygame.display.update()
pygame.quit
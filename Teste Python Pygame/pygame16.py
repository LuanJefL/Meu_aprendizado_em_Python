import pygame

pygame.init()
Largura = 460
Altura = 460
Tela = pygame.display.set_mode((Largura, Altura))
pygame.display.set_caption('Teste')
Relógio = pygame.time.Clock()
Relógio_Fps = pygame.time.Clock()
Tick = pygame.time
Running = True
Fps = 60
Segundo = 0
Temp_p_imp = 3


while Running:
    Relógio.tick(Fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    Tela.fill('orange')

    Segundo += Relógio.get_time() / 1000
    if Segundo >= Temp_p_imp:
        print(Segundo)
        Temp_p_imp += 3
        print(Temp_p_imp)
    #print(Segundo)
    
    
    pygame.display.update()
pygame.quit

import pygame

pygame.init()
Largura = 460
Altura = 460
Tela = pygame.display.set_mode((Largura, Altura))
pygame.display.set_caption("Teste")
Relógio = pygame.time.Clock()
Running = True
Tamanho = 10
Verde_Esuro = (0, 175, 0)




while Running:
    Relógio.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    Tela.fill("green")

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
            
            for Quantidade_de_casash in range(0, int((Altura / Tamanho) / 2)):
                Retángulo = pygame.draw.rect(Tela, Cor, (Posição_x, Posição_y, Tamanho, Tamanho), 0)
                Posição_y += Tamanho * 2
    Xadrez(Largura, Altura, Tamanho, Verde_Esuro)


    pygame.display.update()
pygame.quit()
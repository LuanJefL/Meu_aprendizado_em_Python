import pygame

pygame.init()
Tela = pygame.display.set_mode((640, 320))
Running = True
pygame.display.set_caption('Programa')

while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    #Onde vai ser escrito
    pygame.display.update()
pygame.quit()

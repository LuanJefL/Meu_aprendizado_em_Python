import pygame

pygame.init()
Tela = pygame.display.set_mode((640, 320))
Running = True
pygame.display.set_caption('Programa')

while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            print(pygame.key.name())
    pygame.draw.rect(Tela, 'Blue', (305, 135, 30, 50), 1) 
    pygame.draw.line(Tela, 'red', (319, 0), (319, 640), 10) 
    pygame.draw.circle(Tela, 'Blue', (320, 160), 1) 
    
    
    
    pygame.display.update()
pygame.quit()

import pygame

pygame.init()
Largura = 460
Altura = 600
Tela = pygame.display.set_mode((Largura, Altura))
pygame.display.set_caption("Teste")
Relógio = pygame.time.Clock()
Fps = 60
Running = True
a = 20
l = 20
x = (Largura / 2) - (l / 2)
y = (Altura / 2) - (a / 2)


while Running:
    Relógio.tick(Fps)
    for event in pygame.event.get():
        Keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            print(Keys[pygame.K_w])
    Tela.fill('Blue')
    
    pygame.draw.rect(Tela, 'red', (x, y, l, a), 0)

    
    if Keys[pygame.K_w]:
        y -= 6.33333333
    if Keys[pygame.K_s]:
        y += 6.33333333
    
    pygame.display.update()
pygame.quit()

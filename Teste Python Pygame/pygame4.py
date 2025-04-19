import pygame

pygame.init()
Largura = 640
Altura = 320
Tela = pygame.display.set_mode((Largura, Altura))
pygame.display.set_caption('Programa')
Running = True
Relógio = pygame.time.Clock()



x = 305
y = 0
l = 30
a = 0
while Running:
    Relógio.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    Tela.fill('Orange')
    pygame.draw.rect(Tela, 'Blue', (x, y, l, a), 0) #(x, y, Largura em pixels, altura em pixels) para centralizar basta dividir a largura e o tamanho por dois e subtrair as coordenadas que foram divididas por dois
    pygame.draw.line(Tela, 'red', (319, 0), (319, 640), 10) # Primeiro ponto(x, y) Segundo ponto(x,y) 
    pygame.draw.circle(Tela, 'Blue', (320, 160), 1) #(x, y) e raio do circulo
    
    if y >= Altura:
        y = 0
        if y == 0:
            a = 0
    if a != 50:
        a += 1
    y += 1


    
    
    
    
    pygame.display.update()
pygame.quit()

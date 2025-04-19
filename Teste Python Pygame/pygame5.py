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
y2 = 0
while Running:
    Relógio.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    Tela.fill('Orange')
    def Cobra(x, y, a):
        Triângulo = pygame.draw.rect(Tela, 'Blue', (x, y, l, a), 0) #(x, y, Largura em pixels, altura em pixels) para centralizar basta dividir a largura e o tamanho por dois e subtrair as coordenadas que foram divididas por dois
        return Triângulo
    Cobra(x, y, 50)
    
    
    if y >= Altura - 50:
        if a != 50:
            a += 1
            Cobra(x, y2, a)
        if a == 50:
            a = 0
            y = 0

                
    y += 1
    
    
    
    
    pygame.display.update()
pygame.quit()


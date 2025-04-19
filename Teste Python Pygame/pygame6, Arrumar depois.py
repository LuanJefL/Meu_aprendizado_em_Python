import pygame

#Fragemento aparece quando o retângulo copia passa simultaneamente pela parte de cima 
pygame.init()
Largura = 640
Altura = 320
Tela = pygame.display.set_mode((Largura, Altura))
pygame.display.set_caption('Programa')
Running = True
Relógio = pygame.time.Clock()
Velócidade = 2


x = 300
y = 140
l = 20
t = 40
a = 0
m = 0

while Running:
    Relógio.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    Tela.fill('Orange')
    def Cobra(x, y):
        Triângulo = pygame.draw.rect(Tela, 'Blue', (x, y, l, t), 0) #(x, y, Largura em pixels, altura em pixels) para centralizar basta dividir a largura e o tamanho por dois e subtrair as coordenadas que foram divididas por dois pela largura e pelo tamanho
        return Triângulo
    Cobra(x, y)
    
    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x -= Velócidade
    if keys[pygame.K_d]:
        x += Velócidade
    if keys[pygame.K_s]:
        y += Velócidade
    if keys[pygame.K_w]:
        y -= Velócidade

    if y == Altura - t:
        a = t - (t + t)
    if y >= Altura - t:
        if a != t:
            if keys[pygame.K_w]:
                a -= Velócidade
            if keys[pygame.K_s]:
                a += Velócidade
            Cobra(x, a)
            if x >= Largura - l:
                Cobra(m, a)
            if x <= Largura - Largura:
                Cobra(m, a)
        if a == Altura - Altura:
            y = Altura - Altura
    
    if y == Altura - Altura:
        a = Altura
    if y <= Altura - Altura:
        if a != Altura - t:
            if keys[pygame.K_w]:
                a -= Velócidade
            if keys[pygame.K_s]:
                a += Velócidade
            Cobra(x, a)
            if x <= Largura - Largura:
                Cobra(m, a)
            if x >= Largura - l:
                Cobra(m, a)
        if a == Altura - t:
            y = Altura - t
    
    if x == Largura - l:
        m = l - (l + l)
    if x >= Largura - l:
        if m != Largura - Largura:
            if keys[pygame.K_a]:
                m -= Velócidade
            if keys[pygame.K_d]:
                m += Velócidade
            Cobra(m, y)
        if m == Largura - Largura:
            x = Largura - Largura


    if x == Largura - Largura:
        m = Largura
    if x <= Largura - Largura:
        if m != Largura - l:
            if keys[pygame.K_a]:
                m -= Velócidade
            if keys[pygame.K_d]:
                m += Velócidade
        Cobra(m, y)
        if m == Largura - l:
            x = Largura - l

    pygame.display.update()
pygame.quit()


import pygame

pygame.init()
Largura = 460
Altura = 460
Tela = pygame.display.set_mode((Largura, Altura))
pygame.display.set_caption('Programa')
Running = True
Relógio = pygame.time.Clock()
Fps = 60
Velócidade = 10
Velócidade_y = Velócidade
Velócidade_x = 0
Evitar_colisãoy = True
Evitar_colisãoyx = True
Confirmação_mov = 0
Ações_p_seg = 5


x = 300
y = 140
l = 10
t = 10
a = 0
m = 0

while Running:
    Relógio.tick(Fps)
    if Confirmação_mov != Fps + Ações_p_seg:
        Confirmação_mov += Ações_p_seg
    if Confirmação_mov == Fps + Ações_p_seg:
        Confirmação_mov = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    Tela.fill('Orange')
    def Cobra(x, y):
        Triângulo = pygame.draw.rect(Tela, 'Blue', (x, y, l, t), 0) #(x, y, Largura em pixels, altura em pixels) para centralizar basta dividir a largura e o tamanho por dois e subtrair as coordenadas que foram divididas por dois
        return Triângulo
    
    
    
    def input():
        global Velócidade_x, Velócidade_y, Evitar_colisãoy, Evitar_colisãoyx
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and Evitar_colisãoyx:
            Velócidade_x = Velócidade - (Velócidade + Velócidade)
            Velócidade_y = 0
            Evitar_colisãoyx = False
            Evitar_colisãoy = True
        if keys[pygame.K_d] and Evitar_colisãoyx:
            Velócidade_x = Velócidade
            Velócidade_y = 0
            Evitar_colisãoyx = False
            Evitar_colisãoy = True
        if keys[pygame.K_s] and Evitar_colisãoy:
            Velócidade_y = Velócidade
            Velócidade_x = 0
            Evitar_colisãoyx = True
            Evitar_colisãoy = False
        if keys[pygame.K_w] and Evitar_colisãoy:
            Velócidade_y = Velócidade - (Velócidade + Velócidade)
            Velócidade_x = 0
            Evitar_colisãoyx = True
            Evitar_colisãoy = False
            
    def Movimentação():
        global x, y
        x += Velócidade_x
        y += Velócidade_y    
    
    input()

    if Confirmação_mov == Fps:
        if Velócidade_y != 0 or Velócidade_x != 0:
            if Velócidade_x > 0 or Velócidade_y > 0:
                for Fluidez in range(0, t + 1):
                    if Velócidade_x > 0:
                        Cobra(x + Fluidez, y)
                    if Velócidade_y > 0:
                        Cobra(x, y + Fluidez)
            if Velócidade_x < 0 or Velócidade_y < 0:
                for Fluidez in range(0, -11, -1):
                    if Velócidade_x < 0:
                        Cobra(x + Fluidez, y)
                    if Velócidade_y < 0:
                        Cobra(x, y + Fluidez)
        Movimentação()
    
        
        
        



    if y <= Altura - (Altura + t):
        y = Altura - t
    if y >= Altura:
        y = Altura - Altura
    if x <= Largura - (Largura + l):
        x = Largura - l
    if x >= Largura:
        x = Largura - Largura
    

    
    Cobra(x, y)
    pygame.display.update()
pygame.quit()


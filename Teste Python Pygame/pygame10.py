import pygame
import math

pygame.init()
Largura = 460
Altura = 460
Tela = pygame.display.set_mode((Largura, Altura))
pygame.display.set_caption('Programa')
Running = True
Relógio = pygame.time.Clock()
Fps = 60
Tamanho = 20
Velócidade = Tamanho
Velócidade_c = 1
Velócidade_y = Velócidade
Velócidade_x = 0
Evitar_colisãoy = True
Evitar_colisãoyx = True
Confirmação_mov = 0
Ações_p_seg = 2

x = 240
x2 = 0
Cópia_x = 0
y = 240
y2 = 0
Cópia_y = 0

Verde_Esuro = (0, 175, 0)

while Running:
    Relógio.tick(Fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    Tela.fill('green')

    def Cobra(x, y):
        Triângulo = pygame.draw.rect(Tela, 'Blue', (x, y, Tamanho, Tamanho), 0) #(x, y, Largura em pixels, altura em pixels) para centralizar basta dividir a largura e o tamanho por dois e subtrair as coordenadas que foram divididas por dois
        return Triângulo
    
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
            
            for Quantidade_de_casash in range(0, int(math.ceil((Altura / Tamanho) / 2))):
                Retángulo = pygame.draw.rect(Tela, Cor, (Posição_x, Posição_y, Tamanho, Tamanho), 0)
                Posição_y += Tamanho * 2
    
    Xadrez(Largura, Altura, Tamanho, Verde_Esuro)
    
    
    
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
        #Tem um bug que faz a cobra voltar a direção ccontrária quando se aperta o botões muito rápido 
            
    def Movimentação():
        global x, y
        x += Velócidade_x
        y += Velócidade_y    
    
    input()
    
    
    
    def Movimento():
        global Confirmação_mov, Fps, Ações_p_seg, Cópia_x, x2, x, y, y2, Cópia_y
        if Confirmação_mov <= Fps:
            Confirmação_mov += Ações_p_seg
        if Confirmação_mov >= Fps:
            Cópia_x = x
            x2 = Cópia_x

            Cópia_y = y
            y2 = Cópia_y

            Movimentação()

            if y <= Altura - (Altura + Tamanho):
                y = Altura - Tamanho
            if y >= Altura:
                y = Altura - Altura
            if x <= Largura - (Largura + Tamanho):
                x = Largura - Tamanho
            if x >= Largura:
                x = Largura - Largura
            
        if Confirmação_mov >= Fps:
            Confirmação_mov = 0    
        
    



    

    

    
    
    
    
            
    
    

    Fluidez = Velócidade / math.ceil(Fps / Ações_p_seg)
    
    
    

    if x - Cópia_x == Velócidade:
        x2 += Fluidez
        
    if x - Cópia_x == Velócidade * -1:
        x2 -= Fluidez

    if y - Cópia_y == Velócidade:
        y2 += Fluidez
        
    if y - Cópia_y == Velócidade * -1:
        y2 -= Fluidez

    

    
    Cobra(x2, y2)

    
    
    Movimento()
    pygame.display.update()
pygame.quit()


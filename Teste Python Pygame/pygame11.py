import pygame
import random
import time

pygame.init()
Largura = 460 
Altura = 460
Tela = pygame.display.set_mode((Largura, Altura))
pygame.display.set_caption('Teste')
Relógio = pygame.time.Clock()
Fps = 60
Running = True
Tamanho = 30

x = 0
y = 0
Aleatório_x = 50
Aleatório_y = 50
Aleatóriom_x = 50
Aleatóriom_y = 50
Pontos = 0
Tempos = 0
Morte_c = 5
Segundos = 0
Confirmador = 0
Fonte = pygame.font.SysFont('arial', 20, True, True) #(Fonte, Tamanho, Negrito, Italico)

while Running:
    Relógio.tick(Fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    
    Tela.fill('Orange')

    Messagem = f'Pontos: {Pontos}'
    Tempo = f'Tempo: {Segundos}'
    Texo_formatado = Fonte.render(Messagem, False, 'white') #(String, Anti-serrilhamento, Cor)
    Temporizador = Fonte.render(Tempo, False, 'White')
    

    def Retângulo(x, y, T):
        Retangulo = pygame.draw.rect(Tela, 'Blue', (x, y, T, T), 0)
        return Retangulo

   

    Keys = pygame.key.get_pressed()
    if Keys[pygame.K_w]:
        y -= 10
    if Keys[pygame.K_s]:
        y += 10
    if Keys[pygame.K_a]:
        x -= 10
    if Keys[pygame.K_d]:
        x += 10

    def Fruta_f(Aleatório_x, Aleatório_y):
        Fruta = pygame.draw.rect(Tela, 'red', (Aleatório_x, Aleatório_y, 30, 30), 0)
        return Fruta


    if Retângulo(x, y, Tamanho).colliderect(Fruta_f(Aleatório_x, Aleatório_y)):
        Tamanho += 5
        Pontos += 1
        Aleatório_x = random.randint(0, 440)
        Aleatório_y = random.randint(0, 440)
    if Pontos == 80:
        Running = False
    if Pontos == Morte_c or Segundos != 0 or Tempos != 0:
        Confirmador += 1
        if Pontos == Morte_c:
            Morte_c += 5
        if Confirmador == 1:
            Aleatóriom_x = random.randint(0, 440)
            Aleatóriom_y = random.randint(0, 440)
            while Retângulo(x, y, Tamanho).colliderect(Retângulo(Aleatóriom_x, Aleatóriom_y, Tamanho)):
                    Aleatóriom_x = random.randint(0, 420) + 20
                    Aleatóriom_y = random.randint(0, 420) + 20
        Morte = pygame.draw.rect(Tela, "purple", (Aleatóriom_x, Aleatóriom_y, Tamanho, Tamanho), 0)
        if Retângulo(x, y, Tamanho).colliderect(Morte):
            Running = False
        Tempos += 1
        if Tempos == 60:
            Tempos = 0
            Segundos += 1
        if Segundos == 5:
            Pontos += 1
            Segundos = 0
            Confirmador = 0


        

    
    Retângulo(x, y, Tamanho)
    Tela.blit(Texo_formatado, (0, 0)) #(Texto_formatado, coordenadas )
    Tela.blit(Temporizador, (0, 440))

    pygame.display.update()
pygame.quit

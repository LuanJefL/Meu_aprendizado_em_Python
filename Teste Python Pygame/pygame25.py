import pygame
import sys
import math

# Inicialize o Pygame
pygame.init()

# Defina a largura e altura da tela
largura = 400
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Rotacionando um Quadrado")

# Defina as cores
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# Defina as coordenadas das vértices do quadrado
vertices = [(15, 15), (25, 15), (25, 25), (15, 25)]
vertices2 = [(vertices[0][0], vertices[0][1]), (vertices[1][0], vertices[1][1]), (vertices[2][0], vertices[2][1]), (vertices[3][0], vertices[3][1])]

# Função para rotacionar um quadrado em torno do seu centro
def rotacionar_quadrado(vertices, angulo):
    centro_x = sum(v[0] for v in vertices) / len(vertices)
    centro_y = sum(v[1] for v in vertices) / len(vertices)
    nova_lista_vertices = []
    for v in vertices:
        novo_x = (v[0] - centro_x) * math.cos(angulo) - (v[1] - centro_y) * math.sin(angulo) + centro_x
        novo_y = (v[0] - centro_x) * math.sin(angulo) + (v[1] - centro_y) * math.cos(angulo) + centro_y
        nova_lista_vertices.append((int(novo_x), int(novo_y)))
    return nova_lista_vertices

# Loop principal
angulo = 0
while True:
    for evento in pygame.event.get():
        keys = pygame.key.get_pressed()
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if keys[pygame.K_q]:
                angulo += -5
            if keys[pygame.K_e]:
                angulo += 5

    # Limpe a tela
    tela.fill(branco)

    # Rotacione o quadrado
    vertices_rotacionadas = rotacionar_quadrado(vertices, math.radians(angulo))

    # Desenhe o quadrado rotacionado na tela
    pygame.draw.polygon(tela, vermelho, vertices_rotacionadas)
    print(vertices_rotacionadas)
    pygame.draw.polygon(tela, (0,0,0), vertices2, 1)

    # Atualize a tela
    pygame.display.flip()

    # Atualize o ângulo para próxima iteração
 
#Exemplo de como deve ser.
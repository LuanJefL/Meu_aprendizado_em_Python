import pygame

pygame.init()
Largura = 460
Altura = 460
Tela = pygame.display.set_mode((Largura, Altura))
Camada = pygame.Surface((Largura, Altura), pygame.SRCALPHA)
pygame.display.set_caption("Teste")
Relógio = pygame.time.Clock()
Running = True
Fps = 60

Mudança = True

x = 305
y = 305
x2 = 305
y2 = 305


#def draw_rect_alpha(surface, color, rect):
#    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA) #Forma do retângulo como superficíe
#    pygame.draw.rect(shape_surf, color, shape_surf.get_rect()) #Retângulo(Superficíe que é a área do mesmo, cor e alpha, Adquirir a forma do retângulo dentro da várivel onde contêm o retângulo)
#    surface.blit(shape_surf, rect) #Exibir a superficíe e o retângulo

def Triângulo_normal(x, y, Cor):
    Forma = pygame.draw.rect(Camada, Cor, (x, y, 140, 140), 0)
    return Forma

def Triângulo_alpha(Superficíe, Cor, Rect):
    Forma_Super = pygame.Surface(pygame.Rect(Rect).size, pygame.SRCALPHA)
    pygame.draw.rect(Forma_Super, Cor, Forma_Super.get_rect())
    Superficíe.blit(Forma_Super, Rect)

while Running:
    Relógio.tick(Fps)
    Tela.fill('white')
    Tela.blit(Camada, (0, 0))
    Camada.fill('white')
    Triângulo_alpha(Tela, (0, 0, 255, 50), (x, y, 140, 140))
    Triângulo_alpha(Tela, (255, 0, 0, 50), (x + 20, y, 140, 140))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

    Keys = pygame.key.get_pressed()
    if Keys[pygame.K_a]:
        if Mudança:
            x -= 1
    if Keys[pygame.K_d]:
        if Mudança:
            x += 1
    if Keys[pygame.K_w]:
        if Mudança:
            y -= 1
    if Keys[pygame.K_s]:
        if Mudança:
            y += 1



    pygame.display.flip()
pygame.quit()
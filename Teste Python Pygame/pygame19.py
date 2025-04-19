import pygame

pygame.init()
Largura = 460
Altura = 460
Tela = pygame.display.set_mode((Largura, Altura))
Camada = pygame.Surface((Largura, Altura), pygame.SRCALPHA)
pygame.display.set_caption('Teste')
Relógio = pygame.time.Clock()
Run = True
Fps = 60


x = 0
y = 0

#Hit box
Largura_h = 20
Altura_h = 30

#Física
Tamanho_do_pulo = -5
Velocidade = 5



    

class Física:
    def __init__(self):
        self.G = 9.807
        self.Aceleração_f = 0 
        self.gravity = True
    def Gravidade(self):
        global y
        G = Física().G
        T = Relógio.get_time() / 1000
        F = G * T
        if Física().gravity:
            Física_obj.Aceleração_f += F
            y += Física_obj.Aceleração_f
            

Física_obj = Física()


class Estruturas_Hit_Box:
    def __init__(self):
        self.Colisão = True
        self.Exibir_Hit_Box = True

    def Chão(self, Posição_x, Posição_y, Largura, Altura):
        global Relógio, y, Keys
        Chão_h = (Posição_x, Posição_y, Largura, Altura)

        if self.Exibir_Hit_Box:
            Forma = pygame.draw.rect(Camada, 'white', Chão_h, 1)


        if (Posição_x - Largura_h) < x < (Posição_x + Largura) and (Posição_y - Altura_h) < y < (Posição_y + Altura):
            if self.Colisão:
                Física_obj.Aceleração_f = 0
                y = Posição_y - Altura_h
                Relógio = pygame.time.Clock()
                if Keys[pygame.K_SPACE]:
                    Física_obj.Aceleração_f = Tamanho_do_pulo

    def Plataforma(self, Posição_x, Posição_y, Largura, Altura):
        global Relógio, y, Keys
        Plat_h = (Posição_x, Posição_y, Largura, (Altura / 2))
        Teto_h = (Posição_x, Posição_y + (Altura / 2), Largura, (Altura / 2))

        if self.Exibir_Hit_Box:
            Plat = pygame.draw.rect(Camada, (255,255,255), Plat_h, 1)
            Teto = pygame.draw.rect(Camada, (0,0,255), Teto_h, 1)

        if (Posição_x - Largura_h) < x < (Posição_x + Largura) and (Posição_y - Altura_h) < y < (Posição_y + (Altura / 2)):
            if self.Colisão:
                Física_obj.Aceleração_f = 0
                y = Posição_y - Altura_h
                Relógio = pygame.time.Clock()
                if Keys[pygame.K_SPACE]:
                    Física_obj.Aceleração_f = Tamanho_do_pulo


        if (Posição_x - Largura_h) < x < (Posição_x + Largura) and ((Posição_y + (Altura / 2)) - Altura_h) < y < ((Posição_y + (Altura / 2)) + (Altura / 2)):
            if self.Colisão:
                Física_obj.Aceleração_f = 0
                Relógio = pygame.time.Clock()

    def Parede_Escalavel(self, Posição_x, Posição_y, Largura, Altura):
        global x, y, Relógio, Keys
        Tamanho_do_chão_porcentagem = 3
    
        Parede_E_h = (Posição_x, (Posição_y + (Altura / Tamanho_do_chão_porcentagem)), (Largura / 2), (Altura - (Altura / Tamanho_do_chão_porcentagem)))
        Parede_D_h = (Posição_x + (Largura / 2), (Posição_y + (Altura / Tamanho_do_chão_porcentagem)), (Largura / 2), (Altura - (Altura / Tamanho_do_chão_porcentagem)))
        Chão_h = (Posição_x, Posição_y, Largura, (Altura / Tamanho_do_chão_porcentagem))
    
        if self.Exibir_Hit_Box:
            Parede_E = pygame.draw.rect(Camada, 'white', Parede_E_h, 1)
            Parede_D = pygame.draw.rect(Camada, 'white', Parede_D_h, 1)
            Chão = pygame.draw.rect(Camada, 'white', Chão_h, 1)

        if (Posição_x - Largura_h) < x < (Posição_x + (Largura / 2)) and ((Posição_y + (Altura / Tamanho_do_chão_porcentagem)) - Altura_h) < y < ((Posição_y + (Altura / Tamanho_do_chão_porcentagem)) + (Altura - (Altura / Tamanho_do_chão_porcentagem))):
            if self.Colisão:
                x = Posição_x - Largura_h
                Relógio = pygame.time.Clock()

        if ((Posição_x + (Largura / 2)) - Largura_h) < x < ((Posição_x + (Largura / 2)) + (Largura / 2)) and ((Posição_y + (Altura / Tamanho_do_chão_porcentagem)) - Altura_h) < y < ((Posição_y + (Altura / Tamanho_do_chão_porcentagem)) + (Altura - (Altura / Tamanho_do_chão_porcentagem))):
            if self.Colisão:
                x = Posição_x + Largura
                Relógio = pygame.time.Clock()

        if (Posição_x - Largura_h) < x < (Posição_x + Largura) and (Posição_y - Altura_h) < y < (Posição_y + (Altura / Tamanho_do_chão_porcentagem)):
            if self.Colisão:
                Física_obj.Aceleração_f = 0
                y = Posição_y - Altura_h 
                Relógio = pygame.time.Clock()
                if Keys[pygame.K_SPACE]:
                    Física_obj.Aceleração_f = Tamanho_do_pulo

Estruturas_obj = Estruturas_Hit_Box()



def Hit_box(x, y, Cor):
    if Estruturas_obj.Exibir_Hit_Box:
        Figura = pygame.draw.rect(Camada, Cor, (x, y, Largura_h, Altura_h), 1)

class Sapo(pygame.sprite.Sprite): #pygame.sprite.Sprite é uma class do pygame para esse afim
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.Ataque_animação = False
        self.sprites = []
        for self.adicionar in range(1, 11):
            self.sprites.append(pygame.image.load(fr'C:\Minhas coisas\Vs code\Testes Python\Teste Python Pygame\animation-master\attack_{self.adicionar}.png'))
        self.sprite_atual = 0
        self.image = pygame.transform.scale(self.sprites[int(self.sprite_atual)], (128 * 1.5, 64 * 1.5))

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]


    def update(self):
        
        if self.Ataque_animação:
            self.sprite_atual += 0.2
            if self.sprite_atual >= len(self.sprites):
                self.sprite_atual = 0
                self.Ataque_animação = False
            self.image = pygame.transform.scale(self.sprites[int(self.sprite_atual)], (128 * 1.5, 64 * 1.5))

    

    


todas_as_sprites = pygame.sprite.Group()
Sapo_a = Sapo(70, 345)
todas_as_sprites.add(Sapo_a)

imagem_de_fundo = pygame.transform.scale(pygame.image.load(r'C:\Minhas coisas\Vs code\Testes Python\Teste Python Pygame\animation-master\fondo-pixel-art.webp').convert(), (460, 460))



while Run:
    Relógio.tick(Fps)
    Tela.fill('orange')
    Tela.blit(Camada, (0,0))
    Camada.fill('orange')
    Camada.blit(imagem_de_fundo, (0,0))

    for event in pygame.event.get():
        Keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            Run = False
        if event.type == pygame.KEYDOWN:
            if Keys[pygame.K_q]:
                Sapo_a.Ataque_animação = True

    
    if Keys[pygame.K_a]:
        x -= Velocidade
    if Keys[pygame.K_d]:
        x += Velocidade
    if Keys[pygame.K_LSHIFT]:
        Altura_h = 15
        y += 15
    if not Keys[pygame.K_LSHIFT]:
        Altura_h = 30
    if not Física_obj.gravity:
        if Keys[pygame.K_w]:
            y -= Velocidade
        if Keys[pygame.K_s]:
            y += Velocidade
    
    Física_obj.Gravidade()
    
    
    Estruturas_obj.Chão(0, 440, 460, 20)
    Estruturas_obj.Plataforma(20, 400, 40, 10)
    Estruturas_obj.Parede_Escalavel(390, 340, 10, 100)
    Hit_box(x, y, 'black')
    todas_as_sprites.draw(Camada)
    todas_as_sprites.update()
    
    


    if x <= -20:
        x = 440
    if x >= 460:
        x = 0


    pygame.display.flip()
pygame.quit()

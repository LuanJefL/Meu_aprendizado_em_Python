import pygame
import os
import random
import math

#-------------------------------------------------------------------------------------------#

class Diretório:
    def __init__(self):
        self.Diretório_principal = os.path.dirname(__file__)
        self.Diretório_imagens = os.path.join(self.Diretório_principal, 'animation-master')
        self.Diretório_sons = os.path.join(self.Diretório_principal, 'Efeitos sonoros')


Diretório_obj = Diretório()

#print(Diretório().Diretório_principal)
#print(Diretório().Diretório_imagens)
#-------------------------------------------------------------------------------------------#

class Config:
    def __init__(self):  
        pygame.init()
        pygame.display.set_caption('Dino')    
        self.Largura = 1300        
        self.Altura = 460
        self.Tela = pygame.display.set_mode((self.Largura, self.Altura))
        self.Camada = pygame.Surface((self.Largura, self.Altura), pygame.SRCALPHA)
        self.Relógio = pygame.time.Clock()       
        self.Fps = 60
        self.Run = True

Config_obj = Config()

class Tela:
    def __init__(self):
        self.Azul = (0,0,255)
        self.Verde = (0,255,0)
        self.Vermelho = (255,0,0)
        self.Branco = (255,255,255)
        self.Preto = (0,0,0)
    def Imprimir(self):
        pygame.display.flip()
        Config_obj.Tela.fill(self.Branco)    
        Config_obj.Tela.blit(Config_obj.Camada, (0, 0))
        Config_obj.Camada.fill(self.Branco)     

Tela_obj = Tela()

class Chegagem_e_input:
    def __init__(self):
        self.y = 365
        self.Score = 0
        self.Score_minimo_para_o_prox_som = 100
        self.Hi_score = [0]
        self.Velócidade_padrão = 5
    def Chegar(self):
        for self.event in pygame.event.get():
            self.Keys = pygame.key.get_pressed()
            if self.event.type == pygame.QUIT:
                Config_obj.Run = False
            if self.event.type == pygame.KEYDOWN:
                pass
        if Sprite_obj.Colisões:    
            self.Score += 0.2
        self.Velócidade_padrão += self.Score / 1000000 
        if self.Score >= self.Score_minimo_para_o_prox_som:
            self.Score_minimo_para_o_prox_som += 100
            Som_obj.Score_som.play()


    
Chegagem_e_input_obj = Chegagem_e_input()   

#-------------------------------------------------------------------------------------------#

class Gravidade:
    def __init__(self):
        self.aceleração_f = 0
        self.G = 25.807
        self.Segundos = 0
    def Gravidade_d(self):
        self.Segundos += Config_obj.Relógio.get_time() / 1000
        self.T = Config_obj.Relógio.get_time() / 1000
        self.F = self.G * self.T
        self.aceleração_f += self.F
        Chegagem_e_input_obj.y += self.aceleração_f
        
Gravidade_obj = Gravidade()
#-------------------------------------------------------------------------------------------#

class Texto:
    def __init__(self):
        self.Fonte = pygame.font.SysFont('Arial', 16, True, False)
        
    def Desenhar_texto(self):
        self.Score = f'Score:{int(Chegagem_e_input_obj.Score)}'
        self.Score_msg = self.Fonte.render(self.Score, False, (0,0,0) )
        Config_obj.Camada.blit(self.Score_msg, (Config_obj.Largura - 120, 0))
        self.High_score = f'HI {max(Chegagem_e_input_obj.Hi_score)}'
        self.High_score_msg = self.Fonte.render(self.High_score, False, (0,0,0))
        Config_obj.Camada.blit(self.High_score_msg, (Config_obj.Largura - 300, 0))

Texto_obj = Texto()

#-------------------------------------------------------------------------------------------#

class Som:
    def __init__(self):
        self.Pulo = pygame.mixer.Sound(os.path.join(Diretório_obj.Diretório_sons, 'jump_sound.wav'))
        self.Pulo.set_volume(1)
        self.Morte = pygame.mixer.Sound(os.path.join(Diretório_obj.Diretório_sons, 'death_sound.wav'))
        self.Morte.set_volume(1)
        self.Score_som = pygame.mixer.Sound(os.path.join(Diretório_obj.Diretório_sons, 'score_sound.wav'))
        self.Score_som.set_volume(1)

Som_obj = Som()

#-------------------------------------------------------------------------------------------#
class Sprites:
    class Dinos(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.Animação = False
            self.imagens_dinossauro = []
            for i in range(3):
                img = Sprites().sprite_sheet.subsurface((i*32, 0), (32,32)) #((Posição x, Posição y), (Largura, Altura))
                img = pygame.transform.scale(img, (32*2, 32*2))
                self.imagens_dinossauro.append(img)
            
            self.index_lista = 0
            self.image = self.imagens_dinossauro[self.index_lista]
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)

        def update(self):
            if Chegagem_e_input_obj.y > 365:
                Gravidade_obj.aceleração_f = 0 
                Chegagem_e_input_obj.y = 365
                if Chegagem_e_input_obj.Keys[pygame.K_SPACE]:
                    Gravidade_obj.aceleração_f -= 8
                    self.Animação = False
                    Som_obj.Pulo.play()
                if not Chegagem_e_input_obj.Keys[pygame.K_SPACE]:
                    self.Animação = True

            self.rect.topleft = (40, Chegagem_e_input_obj.y) #40, 365

            if self.Animação:
                if self.index_lista > 2:
                    self.index_lista = 0
                self.index_lista += 0.25
                self.image = self.imagens_dinossauro[int(self.index_lista)]

    class Nuvems(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = Sprites().sprite_sheet.subsurface((32 * 7, 0), (32, 32))
            self.image = pygame.transform.scale(self.image, (32 * 2, 32 * 2))
            self.rect = self.image.get_rect()
            self.rect.y = random.randint(0, (Config_obj.Altura / 4))
            self.rect.x = random.randint(-200, 0)
            
            

        def update(self):
            if self.rect.topright[0] < 0:
                self.rect.x = random.randint(Config_obj.Largura, Config_obj.Largura + 200)
                self.rect.y = random.randint(0, (Config_obj.Altura / 4))
            self.rect.x += -1

    class Cacto(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = Sprites().sprite_sheet.subsurface((32 * 5, 0), (32, 32))
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.y = 380
            self.x = 900 + 64
            
            
            

        def update(self):
            self.rect.topright = (self.x, self.y)


            if Sprite_obj.Colisões:
                self.x -= Chegagem_e_input_obj.Velócidade_padrão

            if self.x < 0 or Chegagem_e_input_obj.Keys[pygame.K_q] and not Sprite_obj.Colisões:
                self.kill()
                
            

    class Pássaro(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.imagens_passaro = []
            self.index = 0
            for self.sprite_pos in range(3, 6):
                self.img = Sprites().sprite_sheet.subsurface((32 * self.sprite_pos, 0), (32, 32))
                self.img = pygame.transform.scale(self.img, (32 * 1.5, 32 * 1.5))
                self.imagens_passaro.append(self.img)
            self.image = self.imagens_passaro[self.index]
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.Velócidade = 5
            self.x = (900 + 64)
            self.y = random.randrange(325, 375, 49)
            

        def update(self):
            self.rect.topright = (self.x, self.y)

            if Sprite_obj.Colisões:
                self.x -= Chegagem_e_input_obj.Velócidade_padrão
                
            
            
            if self.x < 0 or Chegagem_e_input_obj.Keys[pygame.K_q] and not Sprite_obj.Colisões:
                self.kill()
                



            if Sprite_obj.Colisões:
                self.index += 0.10
                if self.index > 2:
                    self.index = 0
                self.image = self.imagens_passaro[int(self.index)]
            

    def __init__(self):
        self.sprite_sheet = pygame.image.load(os.path.join(Diretório_obj.Diretório_imagens, 'dinoSpritesheet.png'))
        self.Todas_sprites = pygame.sprite.Group()
        self.Obstáculos = pygame.sprite.Group()
        self.Enfeite = pygame.sprite.Group()
        self.Colisões = True
        self.x = 0
        self.img = self.sprite_sheet.subsurface((32 * 6, 0), (32, 32))
        self.Quantidade_de_elementos = round(Config_obj.Largura / 32)
        
        

    def ani(self):
        
        
        
        self.Obstáculos.update()
        self.Obstáculos.draw(Config_obj.Camada)
        
        if not self.Colisões:
            if Chegagem_e_input_obj.Keys[pygame.K_q]:
                Chegagem_e_input_obj.Hi_score.append(int(Chegagem_e_input_obj.Score))
                Chegagem_e_input_obj.Score = 0
                print(Chegagem_e_input_obj.Hi_score)

        if pygame.sprite.spritecollide(Objetos_obj.Dino_sprites_obj, self.Obstáculos, False, pygame.sprite.collide_mask):
            if self.Colisões:
                Som_obj.Morte.play()
            self.Colisões = False
            #pass

        if Chegagem_e_input_obj.Keys[pygame.K_q]:
            Chegagem_e_input_obj.Score_minimo_para_o_prox_som = 100
            self.Colisões = True

        if self.Colisões:
            self.Enfeite.update()
            self.Todas_sprites.update()

        for self.Quantidade_de_elementos_f in range(0, self.Quantidade_de_elementos * 2):
            Config_obj.Camada.blit(self.img, ((self.x + (32 * self.Quantidade_de_elementos_f),395)))
        if self.x <= (-32 * (self.Quantidade_de_elementos_f / 2)):
            self.x = -16
        if self.Colisões:
            self.x -= Chegagem_e_input_obj.Velócidade_padrão

        
        self.Todas_sprites.draw(Config_obj.Camada)
        self.Enfeite.draw(Config_obj.Camada)
class Objetos:
        def __init__(self):
            self.Sorteio = 0
            self.Tempo_p_prox_obs = 2
            self.Último_tempo = 0
            for x in range(3):
                self.Nuvem_img_obj = Sprites().Nuvems()
                Sprite_obj.Enfeite.add(self.Nuvem_img_obj)
            self.Dino_sprites_obj = Sprites().Dinos()
            Sprite_obj.Todas_sprites.add(self.Dino_sprites_obj)
        
        def Desenhar(self):
            if Sprite_obj.Colisões:
                if Gravidade_obj.Segundos >= self.Último_tempo:
                    self.Último_tempo += self.Tempo_p_prox_obs
                    self.Sorteio = random.randint(0,1)
                    if self.Sorteio == 0:
                        self.Cacto_obj = Sprites().Cacto()
                        Sprite_obj.Obstáculos.add(self.Cacto_obj)
                    if self.Sorteio == 1:
                        self.Pássaro_sprite_obj = Sprites().Pássaro()
                        Sprite_obj.Obstáculos.add(self.Pássaro_sprite_obj)
            if not Sprite_obj.Colisões:
                self.Último_tempo = 0
                Gravidade_obj.Segundos = 0
                Chegagem_e_input_obj.Velócidade_padrão = 5
                



        
Sprite_obj = Sprites()
Objetos_obj = Objetos()
#-------------------------------------------------------------------------------------------#


class Loop:
    def __init__(self):
        pass
    def Jogo(self):
        while Config_obj.Run:
            Tela_obj.Imprimir()
            Chegagem_e_input_obj.Chegar()
            Texto_obj.Desenhar_texto()
            Objetos_obj.Desenhar()
            Sprite_obj.ani()
            Gravidade_obj.Gravidade_d()
            Config_obj.Relógio.tick(Config_obj.Fps)
        pygame.quit()

Loop_obj = Loop() 


#-----------------------------------------#-#-#-#
Loop_obj.Jogo()
#-----------------------------------------#-#-#-#


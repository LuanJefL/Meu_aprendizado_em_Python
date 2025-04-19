import pygame
import os
import random
import math

#-------------------------------------------------------------------------------------------#

class Diretório:
    def __init__(self):
        self.Diretório_principal = os.path.dirname(__file__)
        self.Diretório_imagens = os.path.join(self.Diretório_principal, 'animation-master')


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
        Config_obj.Relógio.tick(Config_obj.Fps)
        pygame.display.flip()
        Config_obj.Tela.fill(self.Branco)    
        Config_obj.Tela.blit(Config_obj.Camada, (0, 0))
        Config_obj.Camada.fill(self.Branco)     

Tela_obj = Tela()

class Chegagem_e_input:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.Velócidade_padrão = 5
    def Chegar(self):
        for self.event in pygame.event.get():
            self.Keys = pygame.key.get_pressed()
            if self.event.type == pygame.QUIT:
                Config_obj.Run = False
            if self.event.type == pygame.KEYDOWN:
                pass
        if self.Keys[pygame.K_w]:
            self.y -= self.Velócidade_padrão
        if self.Keys[pygame.K_s]:
            self.y += self.Velócidade_padrão
        if self.Keys[pygame.K_a]:
            self.x -= self.Velócidade_padrão
        if self.Keys[pygame.K_d]:
            self.x += self.Velócidade_padrão
    
Chegagem_e_input_obj = Chegagem_e_input()   

#-------------------------------------------------------------------------------------------#

class Gravidade:
    def __init__(self):
        self.aceleração_f = 0
        self.G = 25.807
    def Gravidade_d(self):
        self.T = Config_obj.Relógio.get_time() / 1000
        self.F = self.G * self.T
        self.aceleração_f += self.F
        Chegagem_e_input_obj.y += self.aceleração_f
        
Gravidade_obj = Gravidade()

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
                Config_obj.Relógio = pygame.time.Clock()
                if Chegagem_e_input_obj.Keys[pygame.K_SPACE]:
                    Gravidade_obj.aceleração_f -= 8
                    self.Animação = False
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
            
    class Chão(pygame.sprite.Sprite):
        def __init__(self, pos_x):
            super().__init__()
            self.image = pygame.transform.scale(Sprites().sprite_sheet.subsurface((32 * 6, 0), (32, 32)), (76 , 32))
            self.rect = self.image.get_rect()
            self.rect.topleft = (pos_x * 64, Config_obj.Altura - 64)

        def update(self):
            if self.rect.topright[0] < 0:
                self.rect.x = Config_obj.Largura
            self.rect.x -= 5

    class Cacto(pygame.sprite.Sprite):
        def __init__(self, Mais_x, Parte):
            super().__init__()
            self.image = Sprites().sprite_sheet.subsurface((32 * 5, 0), (32, 32))
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.Mais_x = Mais_x
            self.Parte = Parte
            self.Igualdade = True
            self.y = 380
            self.x = ((900 + 64) + self.Mais_x)
            self.Velócidade = 5
            self.Imovel = True
            
            
            

        def update(self):
            self.rect.topright = (self.x, self.y)

            if not Sprite_obj.Colisões:
                if Chegagem_e_input_obj.Keys[pygame.K_q]:
                    self.x = ((900 + 64) + self.Mais_x)

            if self.x < 0:
                Sprite_obj.Parte[self.Parte] = random.randint(0, 1)
                #pass
            
                
            
            if Sprite_obj.Parte[self.Parte] == 0:
                self.Imovel = False
            if Sprite_obj.Parte[self.Parte] == 1:
                self.Imovel = True

            if Sprite_obj.Parte['Parte1'] == 0 and Sprite_obj.Parte['Parte2'] == 0:
                self.Igualdade = True
            else:
                self.Igualdade = False

            if self.x < 0:
                
                

                if self.Parte == 'Parte1':
                    self.x = ((900 + 64) + self.Mais_x)

                '''if self.Parte != 'Parte1' and not self.Imovel and self.Igualdade:
                    self.x -= Objetos_obj.Distância_entre_os_obstaculos
                if self.Parte != 'Parte1' and self.Imovel and self.Igualdade:
                    self.x = ((900 + 64) + self.Mais_x)
                if self.Parte != 'Parte1' and not self.Imovel and not self.Igualdade:
                    self.x -= Objetos_obj.Distância_entre_os_obstaculos + self.Velócidade
                if self.Parte != 'Parte1' and self.Imovel and not self.Igualdade:
                    self.x = ((900 + 64) + self.Mais_x - self.Velócidade)'''
                if self.Parte != 'Parte1' and self.Imovel:
                    print('Isso')
                    self.x = ((900 + 64) + self.Mais_x - Objetos_obj.Distância_entre_os_obstaculos)
                if self.Parte != 'Parte1' and not self.Imovel and self.Igualdade:
                    self.x = ((900 + 64) + self.Mais_x)
                if self.Parte != 'Parte1' and not self.Imovel and not self.Igualdade:
                    self.x = ((900 + 64) + self.Mais_x)
    
                
           
            if Sprite_obj.Parte[self.Parte] == 0 and not self.Imovel:
                if Sprite_obj.Colisões:
                    self.x -= self.Velócidade

           
                             
            if Chegagem_e_input_obj.Keys[pygame.K_e]:
                if self.Parte == 'Parte1' and not self.Imovel:
                    print(f'{self.Parte}:{self.x}, Cacto')
                if self.Parte == 'Parte2' and not self.Imovel:
                    print(f'{self.Parte}:{self.x}, Cacto')

                
                
                 
            

    class Pássaro(pygame.sprite.Sprite):
        def __init__(self, Mais_x, Parte):
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
            self.Mais_x = Mais_x
            self.Parte = Parte
            self.Imovel = True
            self.Igualdade = True
            self.Velócidade = 5
            self.x = ((900 + 64) + self.Mais_x)
            self.y = random.randrange(325, 375, 49)
            

        def update(self):
            self.rect.topright = (self.x, self.y)

            if not Sprite_obj.Colisões:
                if Chegagem_e_input_obj.Keys[pygame.K_q]:
                    self.x = ((900 + 64) + self.Mais_x)

            if self.x < 0:
                Sprite_obj.Parte[self.Parte] = random.randint(0, 1)
                #pass
            
                
            
            if Sprite_obj.Parte[self.Parte] == 1:
                self.Imovel = False
            if Sprite_obj.Parte[self.Parte] == 0:
                self.Imovel = True

            if Sprite_obj.Parte['Parte1'] == 1 and Sprite_obj.Parte['Parte2'] == 1:
                self.Igualdade = True
            else:
                self.Igualdade = False

            if self.x < 0:
                self.y = random.randrange(325, 375, 49)
                
                if self.Parte == 'Parte1':
                    self.x = ((900 + 64) + self.Mais_x)

                '''if self.Parte != 'Parte1' and not self.Imovel and self.Igualdade:
                    self.x -= Objetos_obj.Distância_entre_os_obstaculos
                if self.Parte != 'Parte1' and self.Imovel and self.Igualdade:
                    self.x = ((900 + 64) + self.Mais_x)
                if self.Parte != 'Parte1' and not self.Imovel and not self.Igualdade:
                    self.x -= Objetos_obj.Distância_entre_os_obstaculos + self.Velócidade
                if self.Parte != 'Parte1' and self.Imovel and not self.Igualdade:
                    self.x = ((900 + 64) + self.Mais_x - self.Velócidade)'''
                if self.Parte != 'Parte1' and self.Imovel:
                    print("Isso")
                    self.x = ((900 + 64) + self.Mais_x - Objetos_obj.Distância_entre_os_obstaculos)
                if self.Parte != 'Parte1' and not self.Imovel and self.Igualdade:
                    self.x = ((900 + 64) + self.Mais_x)
                if self.Parte != 'Parte1' and not self.Imovel and not self.Igualdade:
                    self.x = ((900 + 64) + self.Mais_x)
                

    
            
            if Chegagem_e_input_obj.Keys[pygame.K_f]:
                Sprite_obj.Parte[self.Parte] = random.randint(0, 1)

            if Sprite_obj.Parte[self.Parte] == 1 and not self.Imovel:
                if Sprite_obj.Colisões:
                    self.x -= self.Velócidade

            if Chegagem_e_input_obj.Keys[pygame.K_e]:
                if self.Parte == 'Parte1' and not self.Imovel:
                    print(f'{self.Parte}:{self.x}, Pássaro')
                if self.Parte == 'Parte2' and not self.Imovel:
                    print(f'{self.Parte}:{self.x}, Pássaro')



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
        self.Parte = {'Parte1': 0, 'Parte2': 0}
        
        self.Cacto_ou_Pássaro = None
        

    def ani(self):
        

        self.Todas_sprites.draw(Config_obj.Camada)
        self.Enfeite.draw(Config_obj.Camada)
        self.Obstáculos.draw(Config_obj.Camada)
        self.Obstáculos.update()

        if pygame.sprite.spritecollide(Objetos_obj.Dino_sprites_obj, self.Obstáculos, False, pygame.sprite.collide_mask):
            self.Colisões = True
            #pass

        if Chegagem_e_input_obj.Keys[pygame.K_q]:
            self.Colisões = True

        if self.Colisões:
            self.Enfeite.update()
            self.Todas_sprites.update()

class Objetos:
        def __init__(self):
            self.Distância_entre_os_obstaculos = 0
            for x in range(3):
                self.Nuvem_img_obj = Sprites().Nuvems()
                Sprite_obj.Enfeite.add(self.Nuvem_img_obj)
            for Quantidade_de_chão in range(math.ceil((Config_obj.Largura + 64)/ 64)):
                self.Chão_Sprites_obj = Sprites().Chão(Quantidade_de_chão)
                Sprite_obj.Enfeite.add(self.Chão_Sprites_obj)
            for x in range(0, 2):
                self.Cacto_obj = Sprites().Cacto(x * self.Distância_entre_os_obstaculos, f'Parte{str(x + 1)}')
                Sprite_obj.Obstáculos.add(self.Cacto_obj)
            for x in range(0, 2):
                self.Pássaro_sprite_obj = Sprites().Pássaro(x * self.Distância_entre_os_obstaculos, f'Parte{str(x + 1)}')
                Sprite_obj.Obstáculos.add(self.Pássaro_sprite_obj)
            self.Dino_sprites_obj = Sprites().Dinos()
            Sprite_obj.Todas_sprites.add(self.Dino_sprites_obj)
        
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
            Sprite_obj.ani()
            Gravidade_obj.Gravidade_d()
        pygame.quit()

Loop_obj = Loop() 


#-----------------------------------------#-#-#-#
Loop_obj.Jogo()
#-----------------------------------------#-#-#-#

#Fazer com base na passagem do tempo, coordenadas e mais complexo, deixe para depois.
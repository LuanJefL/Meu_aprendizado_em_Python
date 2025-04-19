import pygame
import os

#-------------------------------------------------------------------------------------------#

class Diretório:
    def __init__(self):
        self.Diretório_principal = os.path.dirname(__file__)

#-------------------------------------------------------------------------------------------#

class Config:
    def __init__(self): 
        pygame.init()  
        pygame.display.set_caption('Dino')   
        self.Largura = 460
        self.Altura = 460
        self.Tela = pygame.display.set_mode((self.Largura, self.Altura))
        self.Camada = pygame.Surface((self.Largura, self.Altura), pygame.SRCALPHA)
        self.Relógio = pygame.time.Clock()
        self.Fps = 60
        self.Run = True

Config_obj = Config()

#-------------------------------------------------------------------------------------------#

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
        Config_obj.Tela.fill(self.Vermelho)
        Config_obj.Tela.blit(Config_obj.Camada, (0, 0))
        Config_obj.Camada.fill(self.Vermelho)

Tela_obj = Tela()

#-------------------------------------------------------------------------------------------#

class Chegagem_e_input:
    def __init__(self):
        self.gravity = True
        self.x = 0
        self.y = 0
        self.Velócidade_padrão = 5
        self.Tamanho_do_pulo_P = -5
    def Chegar(self):
        for self.event in pygame.event.get():
            self.Keys = pygame.key.get_pressed()
            if self.event.type == pygame.QUIT:
                Config_obj.Run = False
            if self.event.type == pygame.KEYDOWN:
                pass
        if self.Keys[pygame.K_a]:
            self.x -= self.Velócidade_padrão
        if self.Keys[pygame.K_d]:
            self.x += self.Velócidade_padrão
        if not self.gravity:
            if self.Keys[pygame.K_w]:
                self.y -= self.Velócidade_padrão
            if self.Keys[pygame.K_s]:
                self.y += self.Velócidade_padrão

    
Chegagem_e_input_obj = Chegagem_e_input()

#-------------------------------------------------------------------------------------------#

class Física:
    def __init__(self):
        self.G = 9.807 
        self.Aceleração_f = 0      
    def Gravidade(self):
        G = Física().G
        T = Config_obj.Relógio.get_time() / 1000
        F = G * T
        if Chegagem_e_input_obj.gravity:
            self.Aceleração_f += F
            Chegagem_e_input_obj.y += self.Aceleração_f
            
Física_obj = Física()

#-------------------------------------------------------------------------------------------#

class Personagem:
    def __init__(self):
        self.Exibir_Hit_Box = True
        self.Largura_h = 20
        self.Altura_h = 30
        self.Azul = (0,0,255)
        self.Verde = (0,255,0)
        self.Vermelho = (255,0,0)
        self.Branco = (255,255,255)
        self.Preto = (0,0,0)
    def Forma(self):
        Ret = pygame.draw.rect(Config_obj.Camada, self.Preto, (Chegagem_e_input_obj.x, Chegagem_e_input_obj.y , self.Largura_h, self.Altura_h), 1)

Personagem_obj = Personagem()

#-------------------------------------------------------------------------------------------#

class Estruturas_Hit_Box:
    def __init__(self):
        self.Colisão = True

    def Chão(self, Posição_x, Posição_y, Largura, Altura):
        Chão_h = (Posição_x, Posição_y, Largura, Altura)

        if Personagem_obj.Exibir_Hit_Box:
            Forma = pygame.draw.rect(Config_obj.Camada, 'white', Chão_h, 1)


        if (Posição_x - Personagem_obj.Largura_h) < Chegagem_e_input_obj.x < (Posição_x + Largura) and (Posição_y - Personagem_obj.Altura_h) < Chegagem_e_input_obj.y < (Posição_y + Altura):
            if self.Colisão:
                Física_obj.Aceleração_f = 0
                Chegagem_e_input_obj.y = Posição_y - Personagem_obj.Altura_h
                if Chegagem_e_input_obj.Keys[pygame.K_SPACE]:
                    Física_obj.Aceleração_f = Chegagem_e_input_obj.Tamanho_do_pulo_P

    def Plataforma(self, Posição_x, Posição_y, Largura, Altura):
        Plat_h = (Posição_x, Posição_y, Largura, (Altura / 2))
        Teto_h = (Posição_x, Posição_y + (Altura / 2), Largura, (Altura / 2))

        if Personagem_obj.Exibir_Hit_Box:
            Plat = pygame.draw.rect(Config_obj.Camada, (255,255,255), Plat_h, 1)
            Teto = pygame.draw.rect(Config_obj.Camada, (0,0,255), Teto_h, 1)

        if (Posição_x - Personagem_obj.Largura_h) < Chegagem_e_input_obj.x < (Posição_x + Largura) and (Posição_y - Personagem_obj.Altura_h) < Chegagem_e_input_obj.y < (Posição_y + (Altura / 2)):
            if self.Colisão:
                Física_obj.Aceleração_f = 0
                Chegagem_e_input_obj.y = Posição_y - Personagem_obj.Altura_h
                if Chegagem_e_input_obj.Keys[pygame.K_SPACE]:
                    Física_obj.Aceleração_f = Chegagem_e_input_obj.Tamanho_do_pulo_P


        if (Posição_x - Personagem_obj.Largura_h) < Chegagem_e_input_obj.x < (Posição_x + Largura) and ((Posição_y + (Altura / 2)) - Personagem_obj.Altura_h) < Chegagem_e_input_obj.y < ((Posição_y + (Altura / 2)) + (Altura / 2)):
            if self.Colisão:
                Física_obj.Aceleração_f = 0

    def Parede_Escalavel(self, Posição_x, Posição_y, Largura, Altura):
        Tamanho_do_chão_porcentagem = 3
    
        Parede_E_h = (Posição_x, (Posição_y + (Altura / Tamanho_do_chão_porcentagem)), (Largura / 2), (Altura - (Altura / Tamanho_do_chão_porcentagem)))
        Parede_D_h = (Posição_x + (Largura / 2), (Posição_y + (Altura / Tamanho_do_chão_porcentagem)), (Largura / 2), (Altura - (Altura / Tamanho_do_chão_porcentagem)))
        Chão_h = (Posição_x, Posição_y, Largura, (Altura / Tamanho_do_chão_porcentagem))
    
        if Personagem_obj.Exibir_Hit_Box:
            Parede_E = pygame.draw.rect(Config_obj.Camada, 'white', Parede_E_h, 1)
            Parede_D = pygame.draw.rect(Config_obj.Camada, 'white', Parede_D_h, 1)
            Chão = pygame.draw.rect(Config_obj.Camada, 'white', Chão_h, 1)

        if (Posição_x - Personagem_obj.Largura_h) < Chegagem_e_input_obj.x < (Posição_x + (Largura / 2)) and ((Posição_y + (Altura / Tamanho_do_chão_porcentagem)) - Personagem_obj.Altura_h) < Chegagem_e_input_obj.y < ((Posição_y + (Altura / Tamanho_do_chão_porcentagem)) + (Altura - (Altura / Tamanho_do_chão_porcentagem))):
            if self.Colisão:
                Chegagem_e_input_obj.x = Posição_x - Personagem_obj.Largura_h

        if ((Posição_x + (Largura / 2)) - Personagem_obj.Largura_h) < Chegagem_e_input_obj.x < ((Posição_x + (Largura / 2)) + (Largura / 2)) and ((Posição_y + (Altura / Tamanho_do_chão_porcentagem)) - Personagem_obj.Altura_h) < Chegagem_e_input_obj.y < ((Posição_y + (Altura / Tamanho_do_chão_porcentagem)) + (Altura - (Altura / Tamanho_do_chão_porcentagem))):
            if self.Colisão:
                Chegagem_e_input_obj.x = Posição_x + Largura

        if (Posição_x - Personagem_obj.Largura_h) < Chegagem_e_input_obj.x < (Posição_x + Largura) and (Posição_y - Personagem_obj.Altura_h) < Chegagem_e_input_obj.y < (Posição_y + (Altura / Tamanho_do_chão_porcentagem)):
            if self.Colisão:
                Física_obj.Aceleração_f = 0
                Chegagem_e_input_obj.y = Posição_y - Personagem_obj.Altura_h 
                if Chegagem_e_input_obj.Keys[pygame.K_SPACE]:
                    Física_obj.Aceleração_f = Chegagem_e_input_obj.Tamanho_do_pulo_P

Estruturas_obj = Estruturas_Hit_Box()

#-------------------------------------------------------------------------------------------#

class Loop:
    def __init__(self):
        pass
    def Jogo(self):
        while Config_obj.Run:
            Tela_obj.Imprimir()
            Chegagem_e_input_obj.Chegar()
            Personagem_obj.Forma()
            Física_obj.Gravidade()
            #------------------------#
            Estruturas_obj.Chão(0, 440, 460, 20)
            Estruturas_obj.Plataforma(20, 400, 40, 10)
            Estruturas_obj.Parede_Escalavel(390, 340, 10, 100)
            #------------------------#
        
        pygame.quit()

Loop_obj = Loop() 

#-----------------------------------------#-#-#-#
Loop_obj.Jogo()
#-----------------------------------------#-#-#-#

    
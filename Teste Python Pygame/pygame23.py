import pygame
import os


#-------------------------------------------------------------------------------------------------------#

class Diretórios:
    def __init__(self):
        self.Diretório_principal = os.path.dirname(__file__)
        self.Diretório_imagens = os.path.join(self.Diretório_principal, 'animation-master')

Diretórios_obj = Diretórios()

#-------------------------------------------------------------------------------------------------------#
class Config:
    def __init__(self):
        pygame.init()
        self.Largura = 1300
        self.Altura  = 460
        pygame.display.set_caption('Teste')
        self.Tela = pygame.display.set_mode((self.Largura, self.Altura))
        self.Camada = pygame.Surface((self.Largura, self.Altura), pygame.SRCALPHA)
        self.Relógio = pygame.time.Clock()
        self.Fps = 60
        self.Azul = (0,0,255)
        self.Verde = (0,255,0)
        self.Vermelho = (255,0,0)
        self.Branco = (255,255,255)
        self.Preto = (0,0,0)
    def Tela_imp(self):
        pygame.display.flip()
        self.Tela.fill(self.Branco)
        self.Tela.blit(self.Camada, (0,0))
        self.Camada.fill(self.Branco)

Config_obj = Config()

#-------------------------------------------------------------------------------------------------------#

class Chegagem_e_input:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.Run = True
    def Verificação(self):
        for self.Event in pygame.event.get():
            self.Keys = pygame.key.get_pressed()
            if self.Event.type == pygame.QUIT:
                self.Run = False

Chegagem_e_input_obj = Chegagem_e_input()

#-------------------------------------------------------------------------------------------------------#

class Estrutura:
    def __init__(self):
        self.Preto = (0,0,0)
        self.x = 0
        self.Sprite_sheet = pygame.image.load(os.path.join(Diretórios_obj.Diretório_imagens, 'dinoSpritesheet.png'))
        self.img = self.Sprite_sheet.subsurface((32 * 6, 0), (32, 32))
        self.Quantidade_de_elementos = round(Config_obj.Largura / 32)


    def Desenhar(self):
        for self.Quantidade_de_elementos_f in range(0, self.Quantidade_de_elementos * 2):
            Config_obj.Camada.blit(self.img, ((self.x + (32 * self.Quantidade_de_elementos_f),365)))
            pygame.draw.rect(Config_obj.Camada, (255,0,0), ((self.x + (32 * self.Quantidade_de_elementos_f)), 0, 1, Config_obj.Altura))
        if self.x <= (-32 * (self.Quantidade_de_elementos_f / 2)):
            print(self.Quantidade_de_elementos_f)
            print(-32 * (self.Quantidade_de_elementos_f / 2))
            print(self.x)
            self.x = -17
        self.x -= 7.549039

        


Estrutura_obj = Estrutura()

#-------------------------------------------------------------------------------------------------------#

class Loop:
    def __init__(self):
        pass
    def Interface(self):
        while Chegagem_e_input_obj.Run:
            Chegagem_e_input_obj.Verificação()
            Config_obj.Tela_imp()
            Estrutura_obj.Desenhar()
            Config_obj.Relógio.tick(Config_obj.Fps)
        pygame.quit()

Loop_obj = Loop()

Loop_obj.Interface()
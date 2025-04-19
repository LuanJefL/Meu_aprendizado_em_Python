import pygame

#-------------------------------------------------------------------------------------------------------#

class Config:
    def __init__(self):
        pygame.init()
        self.Relógio = pygame.time.Clock()
        self.Largura = 460
        self.Altura = 460
        pygame.display.set_caption('Teste')
        self.Tela = pygame.display.set_mode((self.Largura, self.Altura))
        self.Camada = pygame.Surface((self.Largura, self.Altura), pygame.SRCALPHA)
        self.FPS = 60
        self.Branco = (255,255,255)


    def Imprimir(self):
        self.Relógio.tick(self.FPS)
        pygame.display.flip()
        self.Tela.fill(self.Branco)
        self.Tela.blit(self.Camada, (0,0))
        self.Camada.fill(self.Branco)

Config_obj = Config()

#-------------------------------------------------------------------------------------------------------#

class Chegagem_e_input:
    def __init__(self):
        self.Run = True
        self.x = 0
        self.y = 0
        self.Mover_q = False
        self.Mover_e = False

    def Verificação(self):
        for self.events in pygame.event.get():
            self.Keys = pygame.key.get_pressed()
            if self.events.type == pygame.QUIT:
                self.Run = False
            if self.events.type == pygame.KEYDOWN:
                if self.Keys[pygame.K_q]:
                    self.Mover_q = True
                if self.Keys[pygame.K_e]:
                    self.Mover_e = True
        if self.Keys[pygame.K_a]:
            self.x -= 2
        if self.Keys[pygame.K_d]:
            self.x += 2
        if self.Keys[pygame.K_w]:
            self.y -= 2
        if self.Keys[pygame.K_s]:
            self.y += 2


Chegagem_e_input_obj = Chegagem_e_input()

#-------------------------------------------------------------------------------------------------------#

class Gravidade:
    def __init__(self):
        self.G = 9.807
        self.Aceleração_f = 0
    
    def Gravidade_f(self):
        self.T = Config_obj.Relógio.get_time() / 1000
        self.F = self.G * self.T
        self.Aceleração_f += self.F
        '''for self.Quantidade_de_elementos in range(0, len(Elementos_obj.Vertices)):
            if Elementos_obj.Continuação[self.Quantidade_de_elementos]:
                Elementos_obj.Vertices[self.Quantidade_de_elementos][1] += self.Aceleração_f'''
        
Gravidade_obj = Gravidade()

#-------------------------------------------------------------------------------------------------------#

class Elementos:
    def __init__(self):
        self.Branco = (255,255,255)
        self.Preto = (0,0,0)
        self.Velocidade_de_rotação = 1
        self.Vertices = [[20, 10], [30, 20], [20, 30], [10, 20]]
        self.Vertices2 = [[15, 15], [25, 15], [25, 25], [15, 25]]
        self.Vertices3 = [[15, 15], [25, 15], [25, 25], [15, 25]]
        self.Diferencial = [[10, 0], [0, 10]]
        self.Convertor = [[-1, 1], [1, 1], [1, -1], [-1, -1]]
        self.Continuação = [True, True, True, True]

    def Desenhar(self):

        
        '''pygame.draw.line(Config_obj.Camada, self.Preto, self.Vertices[0], self.Vertices[1], 1)
        pygame.draw.line(Config_obj.Camada, self.Preto, self.Vertices[1], self.Vertices[2], 1)
        pygame.draw.line(Config_obj.Camada, self.Preto, self.Vertices[2], self.Vertices[3], 1)
        pygame.draw.line(Config_obj.Camada, self.Preto, self.Vertices[3], self.Vertices[0], 1)'''

        '''pygame.draw.line(Config_obj.Camada, self.Preto, self.Vertices2[0], self.Vertices2[1], 1)
        pygame.draw.line(Config_obj.Camada, self.Preto, self.Vertices2[1], self.Vertices2[2], 1)
        pygame.draw.line(Config_obj.Camada, self.Preto, self.Vertices2[2], self.Vertices2[3], 1)
        pygame.draw.line(Config_obj.Camada, self.Preto, self.Vertices2[3], self.Vertices2[0], 1)'''

        pygame.draw.line(Config_obj.Camada, self.Preto, self.Vertices3[0], self.Vertices3[1], 1)
        pygame.draw.line(Config_obj.Camada, self.Preto, self.Vertices3[1], self.Vertices3[2], 1)
        pygame.draw.line(Config_obj.Camada, self.Preto, self.Vertices3[2], self.Vertices3[3], 1)
        pygame.draw.line(Config_obj.Camada, self.Preto, self.Vertices3[3], self.Vertices3[0], 1)

        
        

        if Chegagem_e_input_obj.Mover_q:
        
            self.Vertices3[0][0] += (self.Velocidade_de_rotação * -1)
            self.Vertices3[0][1] -= (self.Velocidade_de_rotação * -1)
            self.Vertices3[1][0] += (self.Velocidade_de_rotação * -1)
            self.Vertices3[1][1] += (self.Velocidade_de_rotação * -1)
            self.Vertices3[2][0] -= (self.Velocidade_de_rotação * -1)
            self.Vertices3[2][1] += (self.Velocidade_de_rotação * -1)
            self.Vertices3[3][0] -= (self.Velocidade_de_rotação * -1)
            self.Vertices3[3][1] -= (self.Velocidade_de_rotação * -1)

            if int(self.Vertices3[0][0]) <= 10 and int(self.Vertices3[0][1]) >= 20:
                for self.Quantidade_de_Lista in range(0, len(self.Vertices3)):
                    for self.Quantidade_de_Elementos in range(0, len(self.Vertices3[self.Quantidade_de_Lista])):
                        self.Vertices3[self.Quantidade_de_Lista][self.Quantidade_de_Elementos] = round(self.Vertices3[self.Quantidade_de_Lista][self.Quantidade_de_Elementos])
                self.Vertices3.append([int(self.Vertices3[0][0]), int(self.Vertices3[0][1])])
                del self.Vertices3[0]
            print(self.Vertices3)
            
            Chegagem_e_input_obj.Mover_q = False
            

        if Chegagem_e_input_obj.Mover_e:
            

            
                


            self.Vertices3[0][0] += self.Velocidade_de_rotação
            self.Vertices3[0][1] -= self.Velocidade_de_rotação
            self.Vertices3[1][0] += self.Velocidade_de_rotação
            self.Vertices3[1][1] += self.Velocidade_de_rotação
            self.Vertices3[2][0] -= self.Velocidade_de_rotação
            self.Vertices3[2][1] += self.Velocidade_de_rotação
            self.Vertices3[3][0] -= self.Velocidade_de_rotação
            self.Vertices3[3][1] -= self.Velocidade_de_rotação
            
            if int(self.Vertices3[0][0]) >= 20 and int(self.Vertices3[0][1]) <= 10:
                for self.Quantidade_de_Lista in range(0, len(self.Vertices3)):
                    for self.Quantidade_de_Elementos in range(0, len(self.Vertices3[self.Quantidade_de_Lista])):
                        self.Vertices3[self.Quantidade_de_Lista][self.Quantidade_de_Elementos] = round(self.Vertices3[self.Quantidade_de_Lista][self.Quantidade_de_Elementos])
                self.Vertices3.insert(0, (self.Vertices3[-1]))
                del self.Vertices3[-1]

            Chegagem_e_input_obj.Mover_e = False

            print(self.Vertices3)


        



Elementos_obj = Elementos()

#-------------------------------------------------------------------------------------------------------#

class Estruturas:
    def __init__(self):
        self.Preto = (0,0,0)

    def Chão(self):
        self.Área_e_local  = (0, Config_obj.Altura - 40, Config_obj.Largura, 40)
        pygame.draw.rect(Config_obj.Camada, self.Preto, self.Área_e_local, 1)

        '''for Quantidades_de_vertices in range(0, len(Elementos_obj.Vertices)):
            #print((0 - 10) < Elementos_obj.Vertices[Quantidades_de_vertices][0] < (0 + (Config_obj.Largura)), ((Config_obj.Altura - 40) - 10) < Elementos_obj.Vertices[Quantidades_de_vertices][1] < ((Config_obj.Altura - 40) + 40))
            if (0 - 10) < Elementos_obj.Vertices[Quantidades_de_vertices][0] < (0 + (Config_obj.Largura)) and ((Config_obj.Altura - 40) - 10) < Elementos_obj.Vertices[Quantidades_de_vertices][1] < ((Config_obj.Altura - 40) + 40):
                if Quantidades_de_vertices == 0 or Quantidades_de_vertices == 1:
                    Elementos_obj.Vertices[Quantidades_de_vertices][1] = (Config_obj.Altura - 40) - Elementos_obj.Diferencial[1][1]
                    Gravidade_obj.Aceleração_f = 0
                    Elementos_obj.Continuação[Quantidades_de_vertices] = False
                if Quantidades_de_vertices == 2 or Quantidades_de_vertices == 3:
                    Elementos_obj.Vertices[Quantidades_de_vertices][1] = (Config_obj.Altura - 40) - Elementos_obj.Diferencial[0][1]
                    Gravidade_obj.Aceleração_f = 0
                    Elementos_obj.Continuação[Quantidades_de_vertices] = False
            
                if not((0 - 10) < Elementos_obj.Vertices[Quantidades_de_vertices][0] < (0 + (Config_obj.Largura)) and ((Config_obj.Altura - 40) - 10) < Elementos_obj.Vertices[Quantidades_de_vertices][1] < ((Config_obj.Altura - 40) + 40)):
                    Elementos_obj.Continuação[Quantidades_de_vertices] = True'''
                
Estruturas_obj = Estruturas()

#-------------------------------------------------------------------------------------------------------#

class Loop:
    def __init__(self):
        pass
    def Loop_p(self):
        while Chegagem_e_input_obj.Run:
            Chegagem_e_input_obj.Verificação()
            Config_obj.Imprimir()
            Gravidade_obj.Gravidade_f()
            Elementos_obj.Desenhar()
            Estruturas_obj.Chão()

Loop_obj = Loop()

#-------------------------------------------------------------------------------------------------------#

Loop_obj.Loop_p()

#-------------------------------------------------------------------------------------------------------#

#Teste falho
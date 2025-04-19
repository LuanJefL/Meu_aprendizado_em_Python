import operator
import math

Velócidade = 10
Ações_p_seg = 8
Movimento_fx = 0
x1 = 320
x2 = 0
Cópia = 0
Velócidade_x = -10
Fps = 60
Confirmação_mov = 0
Q = 0

while True:

    Fluidez = Velócidade / math.ceil(Fps / Ações_p_seg)

    if x1 - Cópia == Velócidade:
        x2 += Fluidez
    if x1 - Cópia == Velócidade * -1:
        x2 -= Fluidez
    
    if x1 >= 460:
        break
    if x1 <= 0:
        break

    print(x1, x2)
        
    if Confirmação_mov <= Fps:
            Confirmação_mov += Ações_p_seg
    if Confirmação_mov >= Fps:
        Cópia = x1
        x2 = Cópia
        x1 += Velócidade_x
    if Confirmação_mov >= Fps:
            Confirmação_mov = 0   
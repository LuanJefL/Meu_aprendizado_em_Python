import random
import sys
A2 = 0
C1 = 0
D1 = 0
C2 = True
B1 = input("Vamos jogar um jogo?")
B2 = "Sim" == B1 or "SIm" == B1 or "SIM" == B1 or "sim" == B1 or "s" == B1 or "S" == B1
if B2 == True:
    print("Que bom!")
    print("Isso é um simples jogo de adivinhação de números, quando for muito alto vai aparecer menor, quando for mais baixo aparecerá mais alto. Ao acertar o número voçê ganha.") 
else:
    print("Que pena")
    sys.exit()
print("Vamos começar")
while C2 != False:
    A1 = (random.randint(1, 100 ))
    while (A1 != A2 ):
        D1 = D1 + 1
        A2 = int(input ("Qual o número?"))
        if A2 < A1:
            print("maior")
        if A2 > A1:
            print("menor")
    print(f"Parabéns seu número de tentativas foi {D1}")
    D1 = 0
    C1 = input("Você que jogar de novo?")
    C2 = "Sim" == C1 or "SIm" == C1 or "SIM" == C1 or "sim" == C1 or "s" == C1 or "S" == C1
else:
    print("Que pena")
    sys.exit()
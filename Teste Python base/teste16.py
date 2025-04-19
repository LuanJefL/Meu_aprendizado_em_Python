A1 = 10
def g1(A2):
   global A1
   try:
        A3 = A1/A2 
   except:
        print("Algo deu errado, escreva outra coisa")
        return A1/5
   else:
        print("Tudo certo")
        return A3
   finally:
        print ("finalizado")
print(g1(0))
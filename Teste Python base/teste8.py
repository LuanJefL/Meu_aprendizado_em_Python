A1 = ['São paulo', 'Porto Alegre', 'Rio grande do Norte']
A2 = None
for i in range(3):
    A2 = A1[i] # Armazena a strinks da A1 em A2.
    if A2 == 'Porto Alegre': 
        continue # A = São Paulo. A =São Paulo, Porto Alegre, Pule essa etapa. A = São Paulo, Rio Grande do Norte.
    print(A2)
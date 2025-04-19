A1 = input("Está chovendo?")
if A1 == "Sim":
    A2 = input("Você tem um guarda chuva?")
else:
    print("saia")
    exit() 
if A2 == "Não":
    print("Espere um pouco")
else:
    print("saia")
    exit()
A3 = "1"
while(A3 != "Não"):
    A3 = input("Está chovendo?")
    if A3 != "Não":
        print("Espere um pouco")
if A3 == "Não":
    print("saia")
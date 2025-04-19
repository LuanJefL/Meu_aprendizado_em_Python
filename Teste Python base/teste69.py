Número_p_decompor = int(input("Qual número deseja decombor?\n"))
Número_p_dividir = 2
Lista_dos_números_primos= []

while Número_p_decompor != 1:
    #print(Número_p_decompor, Número_p_dividir)
    if Número_p_decompor % Número_p_dividir == 0:
        Número_p_decompor /= Número_p_dividir
        Lista_dos_números_primos.append(Número_p_dividir)
    elif Número_p_decompor % Número_p_dividir >= 1:
        Lista_de_divisores = []
        while True:
            #print(Número_p_dividir)
            for Números_p_dividi_f in range(0, Número_p_dividir):
                if Número_p_dividir % (Números_p_dividi_f + 1) == 0:
                    Lista_de_divisores.append(Números_p_dividi_f + 1)
            if 1 in Lista_de_divisores and Número_p_dividir in Lista_de_divisores and Número_p_dividir % 2 >= 1:
                Lista_de_divisores = []
                if Número_p_decompor % Número_p_dividir == 0:
                    break
            if (Número_p_decompor % Número_p_dividir) >= 1:
                Lista_de_divisores = []
                Número_p_dividir += 1


print(Lista_dos_números_primos)
                



    


Lista = [[[[411.25, 412.5, 413.75, 415.0, 416.25, 417.5, 418.75, 420.0]], [[0, 0, 0, 0, 0, 0, 0, 0]]], [[[421.25, 422.5, 423.75, 425.0, 426.25, 427.5, 428.75, 430.0]], [[0, 0, 0, 0, 0, 0, 0, 0]]], [[[431.25, 432.5, 433.75, 435.0, 436.25, 437.5, 438.75, 440.0]], [[0, 0, 0, 0, 0, 0, 0, 0]]]]
for quantidade_listas in range(0, len(Lista)):
        for quantidade_de_lista_2 in range(0, len(Lista[0][0])):
            for quantidade_de_elementos_f in range(0, len(Lista[0][0][0])):
                print(Lista[quantidade_listas][0][quantidade_de_lista_2][quantidade_de_elementos_f])
                print(Lista[quantidade_listas][1][quantidade_de_lista_2][quantidade_de_elementos_f])
#print(Lista[0][1][0])

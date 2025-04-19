Lista = ["Jubileu"]
try:
    index_01 = Lista[0].index("le", 0, -1)
    print(index_01)
    print(Lista[0][0:index_01])
except:
    print("Não há esse elemento na lista")
print(Lista[0][0:])
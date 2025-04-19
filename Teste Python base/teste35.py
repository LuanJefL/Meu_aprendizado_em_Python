import copy
Lista = [["Jubileu", "Irineu"],["Pablo", "Thomas"]]
Lista_01 = copy.deepcopy(Lista)
Lista[1][0] = "Pimbe"
print(Lista_01)
print(Lista)
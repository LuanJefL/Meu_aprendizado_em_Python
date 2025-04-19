Dicionário = {11 : "-",
    12 : "-",
    13 : "-",
    21 : "-",
    22 : "-",
    23 : "-",
    31 : "-",
    32 : "-",
    33 : "-"}
def Estrutura_jogo_da_velha(Dicionário):
    print("    1     2     3"
        "\n       |     |     " 
       f"\nA   {Dicionário[11]}  |  {Dicionário[12]}  |  {Dicionário[13]}  "
        "\n  _____|_____|_____"
        "\n       |     |     "
       f"\nB   {Dicionário[21]}  |  {Dicionário[22]}  |  {Dicionário[23]}    "
        "\n  _____|_____|_____"
        "\n       |     |     "
       f"\nC   {Dicionário[31]}  |  {Dicionário[32]}  |  {Dicionário[33]}    "
        "\n       |     |     "
        )
Estrutura_jogo_da_velha(Dicionário)
# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    listas.py                                            ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2022/11/23 13:59:26 by Jkutkut            /:::===========:::\    #
#    Updated: 2022/11/23 14:10:05 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

from mares import *

if __name__ == "__main__":
    print("Mares1:")
    # Ej1.1:
    print(f" - Longitud: {len(mares1)}")

    # Ej1.2:
    print(f" - Valores: [{', '.join(mares1)}]")

    print("Mares2:")
    # Ej1.3:
    print(f" - Longitud: {len(mares2)}")

    # Ej1.4:
    print(f" - Valores: [{', '.join(mares2)}]")

    print("Mares:")
    # Ej1.5:
    print(f" - Longitud: {len(mares)}")

    # Ej1.6:
    print(f" - Valores: [{', '.join(mares)}]")

    print("Misceláneo:")
    # Ej1.7:
    print("Valores de las posiciones 1, 2, 3 del mares1:")
    print(f"[{', '.join(mares1[:3])}]")

    # Ej1.8:
    print(f"Índice de 'egeo' en mares1: {mares1.index('egeo')}")

    # Ej1.9:
    print("Valores de las posiciones 4, 5, 6 del mares2:")
    print(f"[{', '.join(mares2[4 - 1:])}]")

    # Ej1.10:
    print(f"Índice de 'caspio' en mares2: {mares2.index('caspio')}")

    # Ej1.11:
    print(f"Índice de 'caspio' en mares: {mares.index('caspio')}")


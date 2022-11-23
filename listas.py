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
#    Updated: 2022/11/23 16:03:16 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

from mares import *

'''
Escribe un programa en Python que cree una lista NO protegida llamada mares1
con 6 posiciones (mediterráneo, cantábrico, báltico, adriático, tirreno, egeo).
• Crea otra lista llamada mares2 con 6 posiciones (rojo, muerto, caspio,
    negro, arábigo, sulu).
• Se creará también una lista nueva llamada mares que tenga 12 posiciones que
    serán las 6 posiciones de mares1 más las 6 posiciones de mares2.

El programa mostrará la siguiente información:
'''
if __name__ == "__main__":
    # Listas importadas del archivo mares.py
    print("Mares1:")
    # Ej1.1:La longitud de la lista mares1
    print(f" - Longitud: {len(mares1)}")

    # Ej1.2:Los valores de todas las posiciones de la lista mares1
    print(f" - Valores: [{', '.join(mares1)}]")

    print("Mares2:")
    # Ej1.3:La longitud de la lista mares2
    print(f" - Longitud: {len(mares2)}")

    # Ej1.4:Los valores de todas las posiciones de la lista mares2
    print(f" - Valores: [{', '.join(mares2)}]")

    print("Mares:")
    # Ej1.5:La longitud de la lista mares
    print(f" - Longitud: {len(mares)}")

    # Ej1.6:Los valores de todas las posiciones de mares
    print(f" - Valores: [{', '.join(mares)}]")

    print("Misceláneo:")
    # Ej1.7:Los valores de las posiciones 1, 2 y 3 de mares1
    print("Valores de las posiciones 1, 2, 3 del mares1:")
    print(f"[{', '.join(mares1[:3])}]")

    # Ej1.8:El índice o posición del mar ‘egeo’ en mares1
    print(f"Índice de 'egeo' en mares1: {mares1.index('egeo')}")

    # Ej1.9:Los valores de las posiciones 4, 5 y 6 de mares2
    print("Valores de las posiciones 4, 5, 6 del mares2:")
    print(f"[{', '.join(mares2[4 - 1:])}]")

    # Ej1.10:El índice o posición del mar caspio en mares2
    print(f"Índice de 'caspio' en mares2: {mares2.index('caspio')}")

    # Ej1.11:El índice o posición del mar caspio en mares
    print(f"Índice de 'caspio' en mares: {mares.index('caspio')}")


# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    modlistas.py                                         ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2022/11/23 14:00:02 by Jkutkut            /:::===========:::\    #
#    Updated: 2022/11/23 18:42:33 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

from mares import *

'''
Escribe un programa en Python que modifique la lista mares siguiendo el orden
siguiente:
'''
if __name__ == "__main__":
    # Ej2.1:Cambia a la vez los valores de los elementos undécimo y duodécimo de
    # la lista mares por los valores 'del norte' y 'alborán'. Muestra la lista
    # mares
    mares[10] = 'del norte'
    mares[11] = 'alborán'
    print(f"Mares:\n[{', '.join(mares)}]")

    # Ej2.2:En la lista mares, inserta un elemento más con el valor 'báltico'. Muestra la lista mares
    mares.append('báltico')
    print(f"Mares:\n[{', '.join(mares)}]")

    # Ej2.3:Borra el quinto elemento de la lista mares. Muestra la lista mares
    mares.pop(4)
    print(f"Mares:\n[{', '.join(mares)}]")

    # Ej2.4:Muestra la longitud de la lista mares
    print("Longitud mares:", len(mares))

    # Ej2.5: Muestra los valores repetidos en la lista mares usando el 
    # método correspondiente
    elementos = set()
    repetidos = set()
    for mar in mares:
        if mar in elementos:
            if not mar in repetidos:
                repetidos.add(mar)
        else:
            elementos.add(mar)

    if len(repetidos) == 0:
        print("No hay mares repetidos en mares")
    else:
        if len(repetidos) == 1:
            print("El mar repetido es: ", end="")
        else:
            print("Los mares repetidos son: ", end="")
        print(*repetidos, sep=", ")

    # Ej2.6:Elimina el tercer elemento de la lista mares y guárdalo en la variable mar1
    mar1 = mares.pop(2)

    # Ej2.7:Elimina el último elemento de la lista mares y guárdalo en la variable mar2
    mar2 = mares.pop(-1)

    # Ej2.8:Guarda el valor del noveno elemento en la variable mar3
    mar3 = mares.pop(8)

    # Ej2.9:Muestra los valores de las variables mar1, mar2 y mar3
    print(*[f"mar{i}: {eval('mar' + str(i))}" for i in range(1, 3+1)], sep="\n")

    # Ej2.10:Elimina el primer elemento de la lista mares con valor 'báltico'. Muestra la lista mares
    if 'báltico' in mares:
        mares.remove('báltico')
    else:
        print('No existe el mar báltico en mares')
    print(mares)

    # Ej2.11:Elimina todos los elementos de la lista mares
    mares.clear()


    # Ej2.12:Ordena por orden alfabético de 'a' a 'z' los elementos de la lista mares1
    print(mares1)
    mares1.sort()
    print(mares1)

    # Ej2.13:Ordena por orden alfabético de 'z' a 'a' los elementos de la lista mares2
    print(mares2)
    mares2.sort(reverse=True)
    print(mares2)


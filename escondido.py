# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    escondido.py                                         ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2022/11/23 21:14:06 by Jkutkut            /:::===========:::\    #
#    Updated: 2022/11/24 09:12:29 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

from random import randint

def askInt(question: str, minimum = None, maximum = None) -> float:
    while True:
        try:
            nbr = int(input(question))
            if minimum != None and nbr < minimum:
                print("El valor tiene que ser mayor que", minimum)
                continue
            elif maximum != None and nbr > maximum:
                print("El valor tiene que ser menor que", maximum)
                continue
            return nbr
        except ValueError:
            print("El valor tiene que ser un número entero.")

MIN = 1
MAX = 10

'''
Escribe un programa en Python que permita calcular el número que esconde. 
El usuario debe averiguar qué número esconde el programa. Se pide números al
usuario y se le informará de si el número es más grande o es más pequeño que
el número a averiguar. Si lo acierta, se le informará con el mensaje
correspondiente.

Muestra cuántas veces ha introducido un número erróneo el usuario hasta dar
con el número correcto. Una vez descubierto, si lo ha acertado en el primer
intento, se mostrará el mensaje “¡Enhorabuena! Lo has acertado a la primera”,
si el número de veces es mayor que 3, se mostrará el mensaje: “Por fin lo has
acertado. Ha debido ser muy complicado para ti”. En otros casos, se mostrará
el mensaje: “Buen Trabajo! Lo has acertado”.
'''
if __name__ == "__main__":
    failedAttempts = 0
    running = True
    solution = randint(MIN, MAX)
    while running:
        nbr = askInt("Introduce un número: ", MIN, MAX)
        if nbr < solution:
            print(f"El número es más grande que {nbr}")
        elif nbr == solution:
            if failedAttempts == 0:
                print("¡Enhorabuena! Lo has acertado a la primera")
            elif failedAttempts <= 3:
                print("Buen Trabajo! Lo has acertado")
            else:
                print("Por fin lo has acertado.")
            running = False
        else:
            print(f"El número es más pequeño que {nbr}")
        failedAttempts += 1

# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    conversortemp.py                                     ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2022/11/23 20:40:43 by Jkutkut            /:::===========:::\    #
#    Updated: 2022/11/24 09:13:01 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

def askFloat(question: str, minimum = None, maximum = None) -> float:
    while True:
        try:
            nbr = float(input(question))
            if minimum != None and nbr < minimum:
                print("El valor tiene que ser mayor que", minimum)
                continue
            elif maximum != None and nbr > maximum:
                print("El valor tiene que ser menor que", maximum)
                continue
            return nbr
        except ValueError:
            print("El valor tiene que ser un número decimal.")

def askStringIn(question: str, options: str) -> str:
    options = [e.upper() for e in options]
    question = f"{question} [{', '.join(options)}] "
    while True:
        s = input(question).strip().upper()
        if s not in options:
            print("Opción inválida")
            continue
        return s

CONVERSORS = {
    # (0 °C × 9 / 5) + 32 = 32 °F
    'C': lambda t: (t * 9 / 5) + 32,
    'F': lambda t: (t - 32) * 5 / 9
}

'''
Escribe un programa en Python que convierta la temperatura dada en grados
Fahrenheit, si se indica que son grados Celsius, o en grados Celsius, si se
indica que son grados Fahrenheit.
'''
if __name__ == "__main__":
    initialUnit = askStringIn(
        'Qué unidades quieres convertir?',
        CONVERSORS.keys()
    )
    finalUnit = 'C' if initialUnit == 'F' else 'F'

    initialTemp = askFloat(f'Temperatura (grados {initialUnit}º): ')
    finalTemp = CONVERSORS[initialUnit](initialTemp)

    print(f"{initialTemp:.2f}º{initialUnit} son {finalTemp:.2f}º{finalUnit}")


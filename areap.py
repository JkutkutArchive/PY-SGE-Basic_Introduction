# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    areap.py                                             ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2022/11/23 18:45:51 by Jkutkut            /:::===========:::\    #
#    Updated: 2022/11/23 21:28:55 by Jkutkut            '-----------------'    #
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

'''
Escribe un programa en Python que calcule el área y el perímetro de un
rectángulo pidiendo al usuario que introduzca la base y la altura del mismo
(con decimales).
'''
if __name__ == "__main__":
    base, height = (askFloat("Base: ", 0), askFloat("Altura: ", 0))
    area = base * height
    perimeter = 2 * (base + height)

    print("Área:", area)
    print("Perímetro", perimeter)

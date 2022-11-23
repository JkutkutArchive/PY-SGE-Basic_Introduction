# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    masquecien.py                                        ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2022/11/23 18:45:51 by Jkutkut            /:::===========:::\    #
#    Updated: 2022/11/23 19:37:42 by Jkutkut            '-----------------'    #
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

N = 2
if __name__ == "__main__":
    s = sum([askFloat(f"Introduce el número {i}/{N}: ") for i in range(1, N+1)])
    if s > 100:
        print("La suma supera la centena.")
    else:
        print(f"La suma ({s}) no supera la centena.")


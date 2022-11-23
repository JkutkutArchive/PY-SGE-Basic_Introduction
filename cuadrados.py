# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    cuadrados.py                                         ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2022/11/23 18:43:59 by Jkutkut            /:::===========:::\    #
#    Updated: 2022/11/23 18:45:20 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

'''
Escribe un programa en Python que cree una lista con los cuadrados de todos los
números enteros del 0 al 10.
'''
if __name__ == "__main__":
    lista = [i * i for i in range(10+1)]
    print(lista)

# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    sumaparimpar.py                                      ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2022/11/23 20:22:33 by Jkutkut            /:::===========:::\    #
#    Updated: 2022/11/23 20:39:16 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

'''
Genera y muestra los números del 1 al 100 y calcula la suma de todos los 
números pares, por un lado, y la suma de los números impares, por otro.
Muestra los resultados.
'''
if __name__ == "__main__":
    # Versión lenta
    # pares = 0
    # impares = 0
    # for i in range(1, 100+1):
    #     print(i, end=" ")
    #     if i % 2 == 1:
    #         impares += i
    #     else:
    #         pares += i

    # print("\nSuma pares:", pares)
    # print("Suma impares:", impares)

    # ------------------------------------------
    # Versión optimizada
    print(*[i for i in range(1, 100+1)], sep=" ")
    print()
    '''
    pares:
       0  2  4 ... 100 = sumaPares
     100 98 97 ...   0 = sumaPares
    --------------------------------
    2 sumaPares = 50 * 100 => sumaPares = 100 * 50 / 2
    Para n => sumPares(n) = n * (n / 2) / 2 = n * n / 4

    De manera equivalente:
    sumaImpares = 1 3 5 ... 99
    sumaImpares = 99 97 ...  1
    ----------------------------
    2 sumaImpares = 100 * 50 =>
    => sumaImpares(n) = n * n / 4
    '''
    print("Suma pares:", (100 * 100) >> 2)
    print("Suma impares:", (100 * 100) >> 2)

import os
os.system("cls")

#Peça dois números ao usuário e os exiba em ordem crescente se o primeiros for menor que o segundo ou em ordem decrescente se o primeiro numero for maior que o segundo.

n1 = int(input("N° 1: ")) #5
n2 = int(input("N° 2: ")) #8

if (n1 <= n2):
    for cresc in range(n1, n2 + 1, 1):
        print(f"{cresc} ", end= " ")
else:
    for decresc in range(n1, n2 - 1, -1):
        print(f"{decresc} ", end= " ")
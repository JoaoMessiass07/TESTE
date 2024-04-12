import os
os.system("cls")

#Peça dois numeros ao usuário e os exiba em ordem crescente. Se o primeiro for maior do que o segundo número, exiba o intervalo da mesma forma.

#Entrada 1: 5 8  Saída1: 5 6 7 8 

n1 = int(input("N° 1: ")) #5
n2 = int(input("N° 2: ")) #8

for cresc in range(n1, n2 + 1, 1):
   print(f"{cresc} ", end= " ")

for decresc in range(n2, n1 + 1, 1):
   print(f"{decresc} ", end= " ")
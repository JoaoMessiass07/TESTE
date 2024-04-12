import os
os.system("cls")

#Peça dois numeros ao usuário e os exiba em ordem crescente. Se o primeiro for maior do que o segundo número, exiba o intervalo da mesma forma.

#Entrada 1: 5 8  Saída1: 5 6 7 8 

num1 = int(input("N° 1: ")) #5
num2 = int(input("N° 2: ")) #8

if num2 < num1:
    aux = num1
    num1 = num2
    num2 = aux

for i in range(num1, num2 + 1, 1):
    print(i, end = ' ')

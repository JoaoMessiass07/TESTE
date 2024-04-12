import os

os.system("cls")

#Peça dois números ao usuário e a ordem ("C"rescente ou "D"decrescente) e exiba o intervalo devido.

num1 = int(input("N° 1: ")) #5
num2 = int(input("N° 2: ")) #8
ordem = str(input("<C>rescente ou <D>ecrescente: "))

if num1 < num2:
    menor = num1
    maior = num2
else:
    menor = num2
    maior = num1

if ordem == 'c' or ordem == 'C':
    for i in range(menor, maior + 1, 1):
        print(i, end = ' ')
elif ordem.upper() == "D":
    for i in range(maior, menor - 1, -1):
        print(i, end = ' ')
else:
    print("Opção inválida!!")
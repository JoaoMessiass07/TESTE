import os

os.system("cls")

#Peça dois números ao usuário e a ordem ("C"rescente ou "D"decrescente) e exiba o intervalo devido.

n1 = int(input("N° 1: ")) #5
n2 = int(input("N° 2: ")) #8
ordem = str(input("<C>rescente ou <D>ecrescente: "))

if ordem == 'C' or ordem == 'c':
    if( n1 == n2 ):
        print("Números digitados são iguais!")
    else: 
        for cresc in range(n1, n2 + 1, 1):
            print(f"{cresc} ", end= " ")

        for cresc in range(n2, n1 + 1, 1):
            print(f"{cresc} ", end= " ")
elif ordem == 'D' or ordem == 'd':
    if( n1 == n2 ):
        print("Números digitados são iguais!")
    else: 
        for decresc in range(n1, n2-1, -1):
            print(f"{decresc} ", end= " ")
        
        for decresc in range(n2, n1-1, -1):
            print(f"{decresc} ", end= " ")
else:
    print("Opção inválida!!")
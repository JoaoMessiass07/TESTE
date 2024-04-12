#Exemplo de aplicacao em laço
import os
os.system("cls")

#valor inicial, valor final (até um número antes) e incremento
#(1 - valor inicial, 10 - valor final( até um número antes), 1 - incremento (significa o que ele vai fazer))
num = int(input("Número: "))
for volta in range(num, num * 10 + 1 , num):
    print(f"{volta} ", end= " ")

print()

#for volta in range(num, 11, 1):
#   tab = num * volta
#    print(f"{volta} ", end= " ")
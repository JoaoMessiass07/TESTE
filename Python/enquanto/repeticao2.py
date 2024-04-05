import os
os.system("cls")

# exibir em ordem crescente os numeros

num1 = int(input("Primero número: ")) # 2
num2 = int(input("Segundo número: ")) # 8

num1 += 1
num1 -= 1

while num1 < num2:
    print(num1)
    num1 = num1 + 1


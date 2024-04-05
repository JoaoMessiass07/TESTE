import os
os.system("cls")

num1 = int(input("Primero número: ")) # 8
num2 = int(input("Segundo número: ")) # 2

num1 -= 1

while num1 > num2:
    print(f"{num1}")
    num1 = num1 - 1
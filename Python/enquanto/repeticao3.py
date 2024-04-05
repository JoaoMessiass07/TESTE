import os 
os.system("cls")

# digitar um numero
# calcular os múltiplos
# calcular os 10 primeiros múltiplos
i = 1
num = float(input("Número: "))

while i<=10:
    resultado = num * i
    print(f"{num} x {i} = {resultado:.0f}")
    i += 1

    
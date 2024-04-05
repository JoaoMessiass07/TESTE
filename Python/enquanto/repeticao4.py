import os 
os.system("cls")

# digitar um numero
# calcular os múltiplos
# calcular os 10 primeiros múltiplos

i = 1
print("Digite 10 números: ")
num = int(input())
maior = num

while i<10:
    num = int(input())
    if num > maior:
        maior = num
    i = i + 1
    
print(f"Maior = {maior}")
import os
os.system("cls")
v = [45, -89, 32, -12, 33]
"""# 1.Primeiro e Ultimo
print(f"1° Elemento: {v[0]}")
print(f"5° Elemento: {v[4]}")"""

"""# 2.Exibe indice impar
for i in range(0,5,1):
    if (v[i]%2 == 1):
        print(f"Impar = {v[i]}")"""

#3. True = existe no vetor | false = não existe no vetor
#Continuar...
x = int(input("Digite um número: "))
for i in range(0,5,1):
    if x == v[i]:
        print("True, pois o número está no vetor")
    else:
        print("False")

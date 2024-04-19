"""import os
os.system("cls")
#    0    1   2   3   4  <= ÍNDICES
v = [45, 89, 32, 12, 33]
for i in range(0,5,1):
    print(f"{v[i]}")"""

import os
os.system("cls")
#    0    1   2    3   4  <= ÍNDICES
v = [45, -89, 32, -12, 33]

# 1. Primeiro numero do vetor
"""print(f"V = {v[0]}")"""

# 2. Somente os numeros negativos contidos no vetor
"""for i in range(0,5,1):
    if v[i]<0:
        print(f"Negativos = {v[i]}")"""

# 3. Soma dos elementos do valor
"""
print("3. Soma dos elementos")
soma = 0 # Variável acumuladora 
# Toda variável acumuladora deve ser inicializada

for i in range(0,5,1):
    soma += v[i] 
print(f"{soma}")"""

# 4. Média dos elementos
print("4. Média dos elementos")
soma = 0 # Variável acumuladora 
contar = 0
# Toda variável acumuladora deve ser inicializada

for i in range(0,5,1):
    soma += v[i]
    contar += 1
media = soma / contar     
print(f"{media}")


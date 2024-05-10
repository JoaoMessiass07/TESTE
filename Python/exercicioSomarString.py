import os
os.system("cls")

lista = ["ends",56,"FIAP","ester",True,35.78,12,78]

def contarStrings(l:list):
    for l in range(len(lista)):
        print(f"{type(lista[l])}")
    
contarStrings(lista)


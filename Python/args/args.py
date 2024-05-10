def soma_numeros (*args) -> float:

    #args é uma lista - quando temos números de parâmetros indefinidos

    soma = 0
    for i in range(0, len(args),1):
        soma = soma + args[i]
    return soma

# ------------ programa principal --------
import os
os.system("cls")

print(soma_numeros(8,8,8,8))
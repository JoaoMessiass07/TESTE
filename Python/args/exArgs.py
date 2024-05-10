import os
os.system("cls")

def verificar_lista_inteiro(l:list) -> bool:
    # Converter todos os itens da lista em String
    print(lista)
    for i in range(0, len(l),1):
        l[i] = str(l[i])
        
    for i in range(0, len(l),1):
        if l[i].isnumeric() == False:
            return False
        else:
            return True
            
# --------- PROGRAMA PRINCIPAL PARA TESTAR A FUNÇÃO
lista = [5, 8, 4, "Edson",12 ,44]
if verificar_lista_inteiro(lista):
    print("-"*50)
    print("Todos os elementos contidos na lista são inteiros")
    print("-"*50)
else:
    print("-"*50)
    print("Nem todos os elementos contidos no laço são inteiros")
    print("-"*50)

lista = [5, 8, 4, 12, 44]
if verificar_lista_inteiro(lista):
    print("-"*50)
    print("Todos os elementos contidos na lista são inteiros")
    print("-"*50)
else:
    print("-"*50)
    print("Nem todos os elementos contidos no laço são inteiros")
    print("-"*50)
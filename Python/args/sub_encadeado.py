# DEFINIÇÃO DOS SUBALGORITMOS
# Definição da função superior
def media2notas(n1: float, n2: float) -> float:

    def notaValida(n: float) -> bool:
        return n >= 0 and n <= 10

    if notaValida(n1) and notaValida(n2):
        return (n1 + n2) / 2
    else:
        return -1 # retornará -1 caso um dos parâmetros não seja uma nota válida
    
# PROGRAMA PRINCIPAL
nota1 = float(input("Nota 1:")) # 8
nota2 = float(input("Nota 2:")) # 45
retorno = media2notas(nota1, nota2)
if retorno == -1:
    print("Nota(s) inválida(s)!")
else:
    print(f"Média = {retorno}")

nota
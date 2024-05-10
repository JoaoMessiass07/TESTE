
# ------ DEFINIÇÃO DOS SUBALGORITMOS
# Subalgoritmo Filho
def menor3notas(n1: float, n2: float, n3: float) -> float:
    menor = n1
    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3
    return menor
# --- Subalgoritmo PAI
def mediacp(n1: float, n2: float, n3: float) -> float:
    return (n1 + n2 + n3 - menor3notas(n1, n2, n3)) / 2
 
# ------- PROGRAMA PRINCIPAL
cp1 = float(input("Checkpoint 1: "))
cp2 = float(input("Checkpoint 2: "))
cp3 = float(input("Checkpoint 3: "))
print(f"Média dos checkpoints: {mediacp(cp1, cp2, cp3):.1f}") # 0 5 6



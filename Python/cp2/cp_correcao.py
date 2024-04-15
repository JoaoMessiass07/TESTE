import os
os.system("cls")

reprovado = 0
aprovado = 0
media_maxima = 0

for i in range (1, 4, 1):
    print(f"Aluno: {i}")
    print("--------CHECKPOINTS")
    cp1 = float(input("Checkpoint 1: "))
    while cp1 < 0 or cp1 > 10:
        print("Erro! digite uma nota válida!")
        cp1 = float(input("Checkpoint 1: "))
        
    print(cp1)
    cp2 = float(input("Checkpoint 2: "))
    while cp2 < 0 or cp2 > 10:
        print("Erro! digite uma nota válida!")
        cp2 = float(input("Checkpoint 2: "))
        
    print(cp2)
    cp3 = float(input("Checkpoint 3: "))
    while cp3 < 0 or cp3 > 10:
        print("Erro! digite uma nota válida!")
        cp3 = float(input("Checkpoint 3: "))
        
    print(cp3)
    print("Digitou todas as notas válidas!")

    menor = cp1
    if cp2 < menor:
        menor = cp2
    if cp3 < menor:
        menor = cp3
    media_cp = (cp1 + cp2 + cp3 - menor) / 2
    print(f"Média: {media_cp}")
    proporcao_cp = media_cp * 0.2


    print("\n---------CHALLENGE")
    sp1 = float(input("Sprint 1: "))
    nota_invalida = sp1 < 0 or sp1 > 10

    while nota_invalida:
        print("Erro! digite uma nota válida!")
        sp1 = float(input("Sprint 1: "))
        nota_invalida = sp1 < 0 or sp1 > 10

    sp2 = float(input("Sprint 2: "))
    nota_invalida = sp2 < 0 or sp2 > 10

    while nota_invalida:
        print("Erro! digite uma nota válida!")
        sp2 = float(input("Sprint 2: "))
        nota_invalida = sp2 < 0 or sp2 > 10

    media_challenge = (sp1 + sp2) / 2
    print(media_challenge)
    proporcao_sp = media_challenge * 0.2





    print("\n--------GLOBAL SOLUTION")
    gs = float(input("Global Solution: "))
    while gs < 0 or gs > 10:
        print("Erro! digite uma nota válida!")
        gs = float(input("Global solution 1: "))

    proporcao_gs = gs * 0.6

    print("\n======== M É D I A S ========")
    print(f"Chechpoints........: {media_cp}")
    print(f"Challenge..........: {media_challenge}")
    print(f"Global Solution....: {gs}")

    media_final = (proporcao_gs + proporcao_sp + proporcao_cp)

    print(f"\n=====> MÉDIA FINAL : {media_final:.1f} ", end ='')

    if media_final < 6:
        print(f"Reprovado! ;\n")
    else:
        print(f"Aprovado! ;\n")

    input("Digite algo para continuar. . .")

if media_final < 6:
    reprovado += 1
elif media_final >= 6:
    aprovado += 1
    if media_final == 10:
        media_maxima += 1
else:
    print("Valor inválido!")

print(f"===== RELATÓRIO FINAL =====")
print(f"Aprovados.......: {aprovado}")
print(f"Reprovados.......: {reprovado}")
print(f"Notas máximas.......: {media_maxima}")

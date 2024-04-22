# ---- Procedimento ==> Subalgoritmo que não retorna valor ao programa chamador
# ==> Sem passagem de parâmetros
def saudacao1():
    print("Bom dia, usuário")
 
def saudacao2(nome):
    print(f"Bom dia, {nome}")
 
def saudacao3(nome, hora):
    if hora < 12:
        msg = "Bom dia"
    elif hora < 18:
        msg = "Boa tarde"
    else:
        msg = "Boa noite"
    print(f"{msg}, {nome}")
 
# ---- Função ==> Subalgoritmo que retorna valor ao programa chamador
 
 
# ======================== PROGRAMA PRINCIPAL
saudacao1()
saudacao2("Maria")
saudacao3("Fernanda", 19)
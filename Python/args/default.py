def saudacao(usuario: str = "Edson", hora: int = 14) -> None:
    if hora < 12:
        turno = "Bom dia"
    elif hora < 18:
        turno = "Boa tarde"
    else:
        turno = "Boa noite"
    print(f"{usuario}, {turno}! Seja bem à Fiap!")

# ----------- programa principal
import os
os.system("cls")
# assumindo os parametros default
saudacao()
# assumindo parcialmente os parametros default
saudacao("Maria")
# assumindo parcialmente os parametros default
saudacao(hora = 9)
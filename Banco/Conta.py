class Conta:
    def __init__(self, numero, cpf, saldo=0.0, ativo=False):
        self.numero = numero
        self.cpf = cpf
        self.saldo = saldo
        self.ativo = ativo

    def getSaldo(self):
        return self.saldo
    
    def ativar(self):
        if self.ativo == True:
            print("A conta já está ativa")
        else:
            self.ativo = True

    def debitar(self, valor):
        if valor <= 0:
           print("Não é possível debitar o valor")
        elif self.saldo >= valor:
            self.saldo -= valor
        else:
           print("Saldo insuficiente.")

    def creditar(self, valor):
        if valor < 0:
            print("Não é possível creditar um valor negativo.")
        else:
            self.saldo += valor

class Poupanca(Conta): 
    def __init__(self, numero, cpf, diaAniversario, saldo=0, ativo=False):
        super().__init__(numero, cpf, saldo, ativo)
        self.diaAniversario = diaAniversario

    def correcao(self, dataAtual):
        if dataAtual == self.diaAniversario:
            self.saldo += (self.getSaldo * 0.05)

class Corrente(Conta):
    def __init__(self, numero, cpf, contadorTalao=0, saldo=0, ativo=False):
        super().__init__(numero, cpf, saldo, ativo)
        self.contadorTalao = contadorTalao

    def pedirTalao(self):
        if self.contadorTalao < 3:
            self.debitar(30)
            self.contadorTalao += 1
        else:
            print("Limite de talões atingido!")

class Especial(Conta):
    def __init__(self, numero, cpf, limite=1000, saldo=0, ativo=False):
        super().__init__(numero, cpf, saldo, ativo)
        self.limite = limite

    def usarLimite(self, valor):
        if self.limite >= valor:
            self.creditar(valor)
            self.limite -= valor
        else:
            print("Limite insuficiente")
    
class Empresa(Conta):
    def __init__(self, numero, cpf, emprestimo_empresa=10000, saldo=0.0, ativo=True):
        super().__init__(numero, cpf, saldo, ativo)
        self.emprestimo_empresa = emprestimo_empresa


    def pedir_emprestimo(self, valor):
        if self.emprestimo_empresa >= valor:
            self.credito(valor)
            self.emprestimo_empresa -= valor
        else:
            raise ValueError("Empréstimo indisponível do valor solicitado.")


class Estudantil(Conta):
    def __init__(self, numero, cpf, limite_estudantil=5000, saldo=0.0, ativo=True):
        super().__init__(numero, cpf, saldo, ativo)
        self.limite_estudantil = limite_estudantil

    
    def usar_estudantil(self, valor):
        if self.limite_estudantil >= valor:
            self.credito(valor)
            self.limite_estudantil -= valor
        else:
            raise ValueError("Limite estudantil insuficiente.")
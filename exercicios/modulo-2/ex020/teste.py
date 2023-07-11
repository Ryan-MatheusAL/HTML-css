class Televisao:
    def __init__(self):
        self.volume = 10
    def aumentar_volume(self):
        self.volume += 1
    def diminuir_volume(self):
        self.volume -=1

tv = Televisao()
print("Volume ao ligar a tv = ", tv.volume)
tv.aumentar_volume()
print("Volume atual = ", tv.volume)

class Pessoa:
    def __init__(self):
        self.cpf = None
        self.nome = None
        self.numero = None
class funcionario(Pessoa):
    def __init__(self):
        self.matricula = None
        self.salario = None
    def bater_ponto(self):
        self.data = 25/10/2004
        pass
    def fazer_login(self):
        self.login = True

f1 = funcionario()
f1.nome = "Funcionario A"
print(f1.nome)

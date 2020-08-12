class Minha(object):
    def __init__(self):
        self.x = 0
        self.y = 0


meu = Minha()
print(meu.x)

# Associações

class Pessoa(object):
    def __init__(self, nome, peso, cao):
        self.nome =nome
        self.peso = peso
        self.cao = cao

    def treinar(self):
        self.cao.daApatinha()
        self.cao.latir()


class Cachorro(object):
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    def daApatinha(self):
        print('%s extendeu a patinha' %self.nome)
    def latir(self):
        print('AUAUAUAUAUAUAUAU')

rex = Cachorro('Rex', 'marrom')
juan = Pessoa('Juan', 75, rex)

print(juan.cao.latir())
# Objetos e funções



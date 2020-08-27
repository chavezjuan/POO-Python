class Meu_Objeto(object):
    # Construtor - inicializa o objeto. Self se refere a instância dessa classe
    def __init__(self, n, i=0):
        self.nome = n
        self.idade = i
        print('Construtor chamado com sucesso')

    # Método. Referência o objeto que está chamando essa função.
    def imprime(self, x):
        print('Ola meu nome é %s e eu tenho %d anos' % (self.nome, self.idade))
        print(x)


pessoa = Meu_Objeto('Juan', 28)
pessoa.imprime('feito')

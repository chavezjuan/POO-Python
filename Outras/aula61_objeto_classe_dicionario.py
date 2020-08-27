Pessoa = {'Nome': 'Lucas', 'Emprego': 'Advogado', 'Idade': 20, 'Cor de Cabelo': 'Preto'}
Pessoa['Nome'] = 'Juan'
print(Pessoa)

#Outra forma de fazer dicionário utilizando classe, criando um objeto
class Pessoa(object):
    pass

Juan = Pessoa()
Juan.nome = 'Juan'
Juan.emprego = 'Desenvolvedor'
Juan.CordeCabelo = 'Preto'
#Método __dict__ especial, assim como init
print(Juan.__dict__)

# Os objetos são armazenados dentro de um dicionário. A vantagem dos
# objetos é que possuem herança, polimorfismo, encapsulamento e etc ..
# Justamente por esse fato dos objetos serem armazenados em dict, o
# python é uma linguagem lenta.

# Outra forma de criar dicionário
dic = dict(nome = 'Juan', emprego = 'dev')


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

#TODO: Crie um método para retornar as informações formatas com Nome e Idade:    
    def dados_pessoa(self, nome, idade):
      return f"Nome: {nome}, Idade: {idade}"

# Entrada do usuário
nome = input()
idade = int(input())

# TODO: Crie uma instância da pessoa:
p1 = Pessoa(nome, idade)

#TODO: Chame o método para retornar as informações formatadas e imprima o resultado:
dados_pessoa = p1.dados_pessoa(nome, idade)
print(dados_pessoa)
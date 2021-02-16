"""
Recebendo dados do usuário

input() -> todo dado recebido via input() é do tipo String
"""
# Entrada de dados
# print('Qual seu nome? ')
# nome = input()

nome = input('Qual o seu nome? ')

# Exemplo de print 'antigo' Python 2.x
# print('Seja bem-vindo(a) %s' % nome)

# Exemplo de print 'moderno' Python 3.x
# print('Seja bem-vindo(a) {0}' .format(nome))

# Exemplo de print 'mais atual' Python 3.7 >
print(f'Seja bem-vindo(a) {nome} ')

# print('Qual a sua idade? ')
# idade = input()

idade = int(input('Qual a sua idade? '))

# Processamento

# Saída
# Exemplo de print 'antigo' Python 2.x
# print('%s tem %s anos' % (nome, idade))

# Exemplo de print 'moderno' Python 3.x
# print('{0} tem {1} anos' .format(nome, idade))

# Exemplo de print 'mais atual' Python 3.7 >
print(f'{nome} tem {idade} anos')

"""
int(idade) == cast
Cast é a 'conversão' de um tipo de dado para outro
"""
print(f'{nome} nasceu em {2021 - idade} ')

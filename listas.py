"""
Listas:

Listas em Python funcionam como vetores/matrizes em outras linguagens,
com a diferença de serem dinamicos e poderem armazenar qualquer tipo de dado.

As listas em Python são representadas por colchetes: []

# EXEMPLOS

# Podemos facilmente verificar se determinado valor está contido na lista
num = 11

if num in list4:
    print(f'Encontrei o numero {num}')
else:
    print(f'numero {num} não está na lista')

# Podemos facilmente ordenar uma lista
list1.sort()
print(list1)

# Podemos facilmente contar o numero de ocorrencias de um valor em uma lista
print(list1.count(99))
print(list2.count('i'))


# Para adicionar elementos em uma lista utilizamos a função append

print(list1)
list1.append(29)
print(list1)
# Obs: com append só é possível adicionar um elemento por vez

list1.append([8, 4, 12])
print(list1)

if [8, 4, 12] in list1:
    print('Lista encontrada')
else:
    print('Lista não encontrada')

# Para adicionar mais de um elemento em uma lista, utilizamos a função extend
list1.extend([21, 47, 93])
print(list1)

# Podemos inserir um novo elemento na lista informando a posição do índice
# Obs: isso não substitui o valor anterior,
#  o mesmo será deslocado para a direita da lista
list1.insert(2, 'novo valor')
print(list1)

# Podemos facilmente juntar duas listas
list6 = list1 + list4
print(list6)
# list1.extend(list4)

# Podemos facilmente inverter uma lista
# Forma 1
list2.reverse()
print(list2)

# Forma 2
print(list1[::-1])

# Copiar uma lista
list6 = list5.copy()
print(list6)

# Contar elementos em uma lista
print(len(list1))

# Remover o ultimo elemento de uma lista
list5.pop()
print(list5)
# Obs: o pop não somente remove o elemento mas também o retorna
print(list5.pop())
# Podemos remover um elemento pelo indice
# Obs: os elementos a direita do indice serão deslocados para a esquerda
# Obs:  se não houver elemento na posição do indice, retornará um erro
list5.pop(3)
print(list5)

# Podemos remover todos os elementos da lista
print(list5)
list5.clear()
print(list5)

# Podemos repetir os elementos de uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos converter uma string em lista
# Exemplo 1
curso = 'Programação em Python essencial'
print(curso)

curso = curso.split()
print(curso)
# Obs: por padrão o split separa os elementos da lista pelo espaço entre eles.
# Exemplo 2
curso = 'Programação,em,Python,essencial'
print(curso)

curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string
lista6 = ['Programação', 'em', 'Python', 'essencial']

curso = ' '.join(lista6)
print(curso)

curso = '-'.join(lista6)
print(curso)

# Exemplo de lista com vários tipos de dados
list6 = [1, 2.34, True, 'Geek', [1, 2, 3], 464698]

print(list6)
print(type(list6))

# Iterando sobre listas
# Exemplo 1 - Utilizando for

soma = 0
for element in list4:
    print(element)
    soma = soma + element
print(soma)

# Exemplo 2  -Utilizando while
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Fazemos acessos aos elementos de forma indexada
#            0       1        2       3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])  # verde
print(cores[1])  # amarelo
print(cores[2])  # azul
print(cores[3])  # branco

# Fazer acesso aos elementos de forma indexada inversa
print(cores[-1])  # branco
print(cores[-2])  # azul
print(cores[-3])  # amarelo
print(cores[-4])  # verde    
"""

type([])

list1 = [1, 99, 4, 27, 15, 22, 3, 44, 42, 27]

list2 = ['L', 'i', 's', 't', ' ', 'S', 't', 'r', 'i', 'n', 'g', 's']

list3 = ['s']

list4 = list(range(11))

list5 = list('Another String')

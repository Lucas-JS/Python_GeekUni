"""
Ranges

    - Precisamos conhecer o loop for para usar os ranges.
    - Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória,
mas sim de maneira especificada.


Formas gerais:

range(valor_de_parada)

OBS: valor_de_parada não inclusive (inico padrão 0, incremento de 1 em 1)

# Exemplo forma 1:
for num in range(11):
    print(num)

#Forma 2

range(valor_de_inicio. valor_de_parada)
OBS: valor de parada não inclusive (início específicado pelo usuário e passo de 1 em 1)
# Exemplo forma 2:
for num in range(1, 11):
    print(num)

# Forma 3
range(valor_de_inicio, valor_de_parada, passo)
OBS: valor de parada não inclusive (início específicado pelo usuário e passo de 1 em 1)
# Exemplo de forma 3
for num in range(1, 10, 2):
    print(num)

# Forma 4 (inverso)
range(valor_de_inicio, valor_de_parada, passo)
OBS: valor de parada não inclusive (início específicado pelo usuário e passo de 1 em 1)
# Exemplo de forma 4:
for num in range(10, 0, -1):
    print(num)

"""

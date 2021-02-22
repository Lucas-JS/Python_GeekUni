"""
Loop for

Utilizamos loops para iterar sobre sequencias ou sobre valores iteráveis

Exemplos de iteráveis:
    - String
        nome = 'John Wayne'
    - Lista
        lista = [1, 3, 5, 7, 9]
    - Range
        numeros = range(1, 10)
"""
nome = 'John Wayne'

lista = [1, 3, 5, 7, 9]

numeros = range(1, 10)

# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)


# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)


# Exemplo de for 3 (Iterando sobre um range)
"""
range = (valor_inicial, valor_final)
Obs: o valor final não é incluso
"""
for numero in range(1, 10):
    print(numero)


# ========================= OUTROS EXEMPLOS =========================
for tupla in enumerate(nome):
    print(tupla)


for _, valor in enumerate(nome):
    print(valor, end=' ')

qtd = int(input('Quantas vezes esse loop deve rodar? '))

soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o valor {n}/{qtd}: '))
    soma += num

print(f'A soma é de: {soma}')


for _ in range(3):
    for num in range(1, 11):
        print('\U0001F480' * num)

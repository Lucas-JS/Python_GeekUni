"""
Saindo de loops com break

Funciona da mesma forma que nas linguagens C ou Java

Utilizamos break para sair de loops de forma planejada.
"""

# Exemplo 1:

for num in range(1, 11):
    if num == 6:
        break
    else:
        print(num)
print('Sai do loop')

while True:
    comando = input("Digite 'sair' para sair: ")
    if comando == 'sair':
        break

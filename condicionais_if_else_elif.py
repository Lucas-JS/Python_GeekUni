"""
Estruturas condicionais
if, else, elif
"""

idade = 15

if idade > 18:
    print("Pode votar e dirigir")
elif idade < 18 and idade >= 16:
    print("Pode votar")
else:
    print("Não pode votar nem dirigir")

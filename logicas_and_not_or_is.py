"""
Estruturas lógicas
and, not, or, is

Operadores unários: not, is
Operadores binários: and, or
"""

a, b = False, True

if type(a) is type(b):
    print("Mesmo tipo")
else:
    print("Tipos diferentes")


if a or b:
    print("Verdadeiro")


if not(a and b):
    print("bla")

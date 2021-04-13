'''
Crie uma função recursiva que calcule o valor de a (base) elevado a b (expoente)

- Se o expoente for zero, a potência é igual 1 (critério de parada)

- Não considere exponenciação de números negativos
'''

def exponential(a, b):
    if b == 0:
        return 1
    return a * exponential(a, b - 1)

print(exponential(2, 5))
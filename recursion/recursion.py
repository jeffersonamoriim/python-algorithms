def recurcao(i):
    print('recurcao')
    i += 1
    if i == 5:
        return
    
    return recurcao(i)

recurcao(0)

def soma(n):
    if n == 0:
        return 0
    return n + soma(n - 1)

print(soma(5))
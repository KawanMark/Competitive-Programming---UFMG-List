#http://codeforces.com/contest/1213/problem/B

def lilkaw(n, precos):
    precos_ruins = 0
    
    menor_preco = float('inf')
    
    for i in range(n - 1, -1, -1):
        if precos[i] < menor_preco:
            menor_preco = precos[i]
        else:
            precos_ruins += 1
    
    return precos_ruins

t = int(input())

for _ in range(t):
    n = int(input())
    precos = list(map(int, input().split()))
    
    print(lilkaw(n, precos))

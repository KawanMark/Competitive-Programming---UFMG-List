#https://codeforces.com/contest/1241/problem/A

def lilkaw(n):
    if n < 4:
        dist = 4
    else:
        dist = n + 1 if n % 2 == 1 else n
    
    return dist - n
    
q = int(input())
resultados = []
for _ in range(q):
    n = int(input())
    resultados.append(lilkaw(n))
for r in resultados:
    print(r)

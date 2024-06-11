#https://br.spoj.com/problems/MINHOCA/


N, M = map(int, input().split())
prod = []

for _ in range(N):
    prod.append(list(map(int, input().split())))


max_soma = 0

for linha in prod:
    soma_linha = sum(linha)
    if soma_linha > max_soma:
        max_soma = soma_linha


for col in range(M):  
    soma_coluna = sum(prod[linha][col] for linha in range(N))
    if soma_coluna > max_soma:
        max_soma = soma_coluna

 
print(max_soma)




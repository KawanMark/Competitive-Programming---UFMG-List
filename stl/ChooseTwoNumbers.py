#https://codeforces.com/problemset/problem/1206/A

def solve(A, B, todos):
    for a in A:
        for b in B:
            if a + b not in todos:
                return a, b

    return 0, 0


todos = set()

n = int(input())
A = list(map(int, input().split()))
todos.update(A)

m = int(input())
B = list(map(int, input().split()))
todos.update(B)


resposta = solve(A, B, todos)
print(resposta[0], resposta[1])


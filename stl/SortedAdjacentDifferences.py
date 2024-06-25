#https://codeforces.com/contest/1339/problem/B

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    resp = []

    i = 0
    j = n-1

    while i <= j:
        if i != j:
            resp.append(a[j])
        resp.append(a[i])
        i += 1
        j -= 1
    resp.reverse()
    for p in resp:
        print(p, end=' ')
    print()

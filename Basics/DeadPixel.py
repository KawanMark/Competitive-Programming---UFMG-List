#https://codeforces.com/contest/1315/problem/A

def maximo(a,b,x,y):
    area1 = x * b
    area2 = (a - x - 1) * b
    area3 = a * y
    area4 = a * (b - y - 1)

    return max(area1, area2, area3, area4)

n = int(input())

for _ in range(n):
    a, b, x, y = map(int, input().split())
    print(maximo(a,b,x,y))




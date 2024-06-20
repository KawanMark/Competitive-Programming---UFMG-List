#https://codeforces.com/contest/1311/problem/A


def lilkaw(a, b):
    if a == b: return 0
    if a > b:
        if (a - b) % 2 == 0:
            return 1
        else:
            return 2
    else:
        if (a - b) % 2 == 1:
            return 1
        else:
            return 2
        

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(lilkaw(a, b))


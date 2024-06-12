#https://codeforces.com/problemset/problem/1301/A


def lilkaw(a, b, c):
    for i in range(len(a)):
        if c[i] != a[i] and c[i] != b[i]:
            return False
    return True

n = int(input())
for _ in range(n):
    a,b,c = input(), input(), input()
    print("YES" if lilkaw(a, b, c) else "NO")


#https://codeforces.com/gym/101972/problem/A

def swap(a, b):
    return b, a
    


n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    resto = b % a

    if resto == 0:
        swap(a, b)
    else:
        resto = a % 10

    print(f'{a - resto} x {b} + {resto} x {b}')

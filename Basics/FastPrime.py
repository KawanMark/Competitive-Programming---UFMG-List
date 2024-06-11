
#https://judge.beecrowd.com/pt/problems/view/1221


import math

def isPrimo(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

n = int(input())

for _ in range(n):
    x = int(input())
    if isPrimo(x):
        print("Prime")
    else:
        print("Not Prime")






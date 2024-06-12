# https://codeforces.com/contest/149/problem/A


def min_meses(k, cm):
    cm.sort(reverse=True)

    total_cm = 0
    meses = 0

    for i in cm:
        if total_cm >=k:
            break
        total_cm += i
        meses += 1
    
    if total_cm < k:
        return -1
    
    else:
        return meses
    
k = int(input())
cm = list(map(int, input().split()))
print(min_meses(k, cm))

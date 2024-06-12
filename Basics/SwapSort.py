#https://codeforces.com/contest/489/problem/A

def selection_sort(arr):
    n = len(arr)
    swaps = []

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps.append((i, min_idx))
        
        if len(swaps) >= n:
            break

    return swaps

n = int(input())
arr = list(map(int, input().split()))

swaps = selection_sort(arr)

print(len(swaps))
for swap in swaps:
    print(swap[0], swap[1])

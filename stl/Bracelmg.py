#https://br.spoj.com/problems/BRACELMG/

def compute_lps_array(pattern):
    length = 0
    i = 1
    lps = [0] * len(pattern)
    
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(pattern, text):
    m = len(pattern)
    n = len(text)
    
    lps = compute_lps_array(pattern)
    
    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return True
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return False

def lilkaw(seq, brac):
    return kmp_search(seq, brac+brac) or kmp_search(seq, brac[::-1]+brac[::-1])

n = int(input())

for _ in range(n):
    seq, brac = input().split()
    if lilkaw(seq, brac):
        print('S')
    else:
        print('N')

#https://br.spoj.com/problems/PALAVRMG/

def lilkaw(s):
    s = s.lower()
    return s == ''.join(sorted(s)) and len(s) == len(set(s))

n = int(input())

for _ in range(n):
    s = input()
    if lilkaw(s):
        print(f"{s}: O")
    else:
        print(f"{s}: N")

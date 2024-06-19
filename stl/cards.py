#https://codeforces.com/problemset/problem/1220/A


def lilkaw(n, s):
    count_z = s.count('z')
    count_e = s.count('e')
    count_r = s.count('r')
    count_o = s.count('o')
    count_n = s.count('n')

    count_zero = count_z
    count_one = min(count_o - count_zero, count_n, count_e - count_zero)

    result = ['1'] * count_one + ['0'] * count_zero

    print(' '.join(result))

n = int(input().strip())
s = input().strip()

lilkaw(n, s)

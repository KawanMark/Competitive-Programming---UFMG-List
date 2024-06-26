# https://judge.beecrowd.com/pt/problems/view/2653

joias = set()

try:
    while True:
        joia = input()
        joias.add(joia)
except EOFError:
    pass

print(len(joias))



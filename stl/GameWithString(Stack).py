#https://codeforces.com/contest/1104/problem/B

from collections import deque
class Stack:
    def __init__(self):
        self.items = deque()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
def main():
    stack = Stack()

    ispar = 0
    palavra = input()

    for char in palavra:
        if not stack.is_empty() and char == stack.peek():
            stack.pop()
            ispar+=1
        else:
            stack.push(char)
    
    if ispar % 2 == 0:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()

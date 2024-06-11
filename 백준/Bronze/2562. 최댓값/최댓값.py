import sys

A = []

for _ in range(9):
    i = int(sys.stdin.readline())
    A.append(i)

print(f"{max(A)}\n{A.index(max(A))+1}")
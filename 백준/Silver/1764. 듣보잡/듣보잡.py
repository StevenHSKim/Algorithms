import sys

N,M = map(int, sys.stdin.readline().split())

a = set()
for _ in range(N):
  a.add(sys.stdin.readline())

b = set()
for _ in range(M):
  b.add(sys.stdin.readline())

result = sorted(list(a & b))

print(len(result))

# for i in result:
#   print(i)

print("".join(result), end=" ")
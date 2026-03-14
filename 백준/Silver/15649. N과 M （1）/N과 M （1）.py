from itertools import permutations

N,M = map(int, input().split())

list = []
for i in range(1,N+1):
    list.append(i)

p = permutations(list, M)

for i in p:
    print(*i)
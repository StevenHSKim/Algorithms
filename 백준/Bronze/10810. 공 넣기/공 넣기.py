import sys

N,M = map(int, input().split())
list1 = [0] * (N+1)

for _ in range(M):
    i,j,k = map(int, sys.stdin.readline().split())
    
    for x in range(i,j+1):
        list1[x] = k

list1 = list1[1:]

print(*list1)
        
import sys

N,M = map(int, input().split())

list = [x for x in range(1,N+1)]

for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    
    tmp1 = list[a-1]
    tmp2 = list[b-1]
    
    list[a-1] = tmp2
    list[b-1] = tmp1

print(*list)
import sys

a,b = map(int, sys.stdin.readline().split())
arr = [x for x in range(1,a+1)]

for _ in range(b):
    i, j = map(int, sys.stdin.readline().split())
    temp = arr[i-1:j]
    temp.reverse()
    arr[i-1:j] = temp
    
print(*arr)
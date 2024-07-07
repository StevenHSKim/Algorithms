import sys

N = int(input())
arr = [[0 for _ in range(101)] for _ in range(101)] # 원소가 0인 100x100 행렬 생성

for _ in range(N):
    x,y = list(map(int, sys.stdin.readline().split()))
    
    for row in range(x, x+10):
        for col in range(y, y+10):
            arr[row][col] = 1  # 색종이 안 부분을 1로 채우기
            
result = 0

for i in arr:
    result += i.count(1) # 1로 채워진 곳 모두 세기

print(result)
    
import sys
sys.setrecursionlimit(10000)

T = int(input())

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x,y):
    if x<0 or x>=N or y<0 or y>=M:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)
        
        return True
    return False
    
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]
    
    for _ in range(K): # 그래프 만들기
        x,y = map(int, input().split())
        graph[y][x] = 1
    
    count = 0
    for i in range(N):
        for j in range(M):
            if dfs(i,j):
                count+=1
    print(count)
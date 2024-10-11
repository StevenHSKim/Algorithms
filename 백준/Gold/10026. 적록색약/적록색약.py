import copy
from collections import deque

N = int(input())
graph = [list(input()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

def bfs(a,b, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = visited
    queue = deque()
    queue.append((a,b))
    visited[a][b] = 1
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<N and 0<=ny<N and graph[nx][ny]==graph[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx,ny))
                
visited1 = copy.deepcopy(visited)
visited2 = copy.deepcopy(visited)

count1 = 0
count2 = 0

for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            bfs(i,j, visited1)
            count1 += 1
            
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if not visited2[i][j]:
            bfs(i,j,visited2)
            count2 += 1
            
print(f"{count1} {count2}")
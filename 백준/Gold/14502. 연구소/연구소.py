import copy
from collections import deque
from itertools import combinations

N,M = map(int, input().split())
result = []

graph = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    count = 0
    queue = deque()
    copy_graph = copy.deepcopy(graph)
    
    for i in range(len(copy_graph)):
        for j in range(len(copy_graph[0])):
            if copy_graph[i][j] == 2:
                queue.append([i,j])
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<N and 0<=ny<M and copy_graph[nx][ny]==0:
                copy_graph[nx][ny] = 2
                queue.append([nx,ny])
    
    for i in range(len(copy_graph)):
        for j in range(len(copy_graph[0])):
            if copy_graph[i][j] == 0:
                count += 1
    
    result.append(count)

            
flatten = []    
for row in graph:
    for element in row:
        flatten.append(element)

zero = []
for i in range(len(flatten)):
    if flatten[i] == 0:
        zero.append(i)
        

for i in combinations(zero,3):
    l = len(graph[0])
    
    graph[i[0]//l][i[0]%l] = 1
    graph[i[1]//l][i[1]%l] = 1
    graph[i[2]//l][i[2]%l] = 1
    
    bfs()
    
    graph[i[0]//l][i[0]%l] = 0
    graph[i[1]//l][i[1]%l] = 0
    graph[i[2]//l][i[2]%l] = 0
        
print(max(result))
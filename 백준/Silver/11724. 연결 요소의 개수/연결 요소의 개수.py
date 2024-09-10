import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

def dfs(start, depth):
    visited[start] = True
    
    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth+1)
    
# 그래프 그리기
for _ in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = [False] * (N+1)
count = 0

for i in range(1,N+1):
    if not visited[i]:  # 만약 i번째 노드 방문하지 않았을 때
        if not graph[i]:  # 연결된 점이 없으면
            count += 1  # 그냥 count+=1 해서 한 묶음 추가
            visited[i] = True  # 방문처리
        else:  # 연결된 점이 있으면
            dfs(i,0)  # dfs 탐색
            count += 1  # 끝나면 개수 +=1
        
print(count)
    
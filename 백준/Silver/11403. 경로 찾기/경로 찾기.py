from collections import deque

N = int(input())
results = []

graph = []
for _ in range(N):
    row = input().split()
    row = map(int, row)
    row = list(row)
    graph.append(row)

def bfs(graph, start):
    queue = deque([start])
    visited = [False] * N
    results_row = [0 for _ in range(N)]

    while queue:
        v = queue.popleft()

        for i in range(N):
            if graph[v][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True
                results_row[i] = 1

    results.append(results_row)

for start in range(N):
    bfs(graph, start)

for r in results:
    print(*r)
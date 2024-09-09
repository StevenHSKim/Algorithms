N = int(input())
graph = []
count = 0
result = []


# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for _ in range(N):
    graph.append(list(map(int,input().rstrip())))

def dfs(x,y):
    global count
    
    if x<0 or x>=N or y<0 or y>=N:
        return False
    
    if graph[x][y] == 1:  # 한 번 탐색할 때
        count += 1  # 세대수 += 1
        graph[x][y] = 0  # 한 번 지나가면 0으로 변경
        for i in range(4):  # 현재 위치에서 네가지 방향으로 dfs 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:  # 1이면 dfs 탐색
            dfs(i,j)
            result.append(count)  # dfs 내부에서 센 세대수 개수 append
            count = 0  # 다시 count를 0으로 초기화
            
result.sort()

print(len(result))  # 총 단지수 출력 (군집 개수 출력)
for k in result:  # 각 단지의 세대수 출력 (군집 요소 개수 출력)
    print(k)
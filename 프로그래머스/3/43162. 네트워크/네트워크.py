def solution(n, computers):
    
    def dfs(i):
        visited[i] = 1
        for j in range(n):  # j: 컴퓨터 간 연결 (열) 순회
            if computers[i][j] and not visited[j]:
                dfs(j)
    
    answer = 0
    visited = [0 for _ in range(len(computers))]
    for i in range(n):  # i: 각 컴퓨터 (행) 순회
        if not visited[i]:
            dfs(i)
            answer += 1
    
    return answer
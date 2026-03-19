import sys

N, D = map(int, input().split())

shortcuts = [[] for _ in range(D+1)]

for _ in range(N):
    start, end, dist = map(int, input().split())
    
    if end > D:
        continue
    
    if end-start <= dist:
        continue
    
    shortcuts[start].append((end,dist))
    
INF = int(1e9)
dp = [INF] * (D+1)
dp[0] = 0

for i in range(D+1):
    if i <= D:
        for end, dist in shortcuts[i]:
            dp[end] = min(dp[end], dp[i]+dist)
            
    if i < D:
        dp[i+1] = min(dp[i+1], dp[i]+1)
        
print(dp[D])

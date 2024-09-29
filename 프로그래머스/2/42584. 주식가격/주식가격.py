from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        cur = queue.popleft()
        count = 0
        
        for j in queue:
            count += 1
            if cur > j:
                break
        
        answer.append(count)
    
    return answer
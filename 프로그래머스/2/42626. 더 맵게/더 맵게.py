import heapq

def solution(scoville, K):
    count = 0
    mix_scoville = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1
        
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        mix = a+(b*2)
        heapq.heappush(scoville, mix)
        count += 1
        
    return count
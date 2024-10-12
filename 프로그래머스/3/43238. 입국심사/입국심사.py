# return이 시간 -> Binary Search를 시간에 대해 수행

def solution(n, times):
    answer = 0
    start = 1
    end = max(times) * n
    
    while start <= end:
        mid = (start+end)//2
        people = 0
        
        for t in times:
            people += mid // t  # 예측 시간 // 검사 시간 -> 검사한 사람 수
            
            if people >= n:  # 예측한 시간 안에 검사한 사람 수가 전체 사람 수를 넘으면
                break  # 그냥 break
                
        if people >= n:
            answer = mid
            end = mid - 1
        
        else:
            start = mid + 1
        
    return answer
def solution(routes):
    answer = 0
    camera = -30001
    
    routes.sort(key=lambda x:x[1]) # 도착시간 기준으로 정렬
    
    for r in routes:
        if camera < r[0]:
            answer += 1
            camera = r[1]
        
    return answer
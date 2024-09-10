def solution(people, limit):
    people.sort()
    
    count = 0
    start = 0  # 시작 인덱스 
    end = len(people)-1  # 끝 인덱스
    
    while start <= end:  # 시작 < 끝 일때
        if people[start] + people[end] <= limit:  # 처음 + 끝 <= limit 이면
            start += 1  # 둘은 보트 태우고, start 한 칸 증가
            end -= 1  # end 한 칸 감소
        else:  # 처음 + 끝 > limit 이면
            end -= 1  # end 인덱스 한 칸 감소
        count += 1  # 한 번 비교 끝나면, 기존 end가 보트 혼자 타거나, 둘이 짝지어 보트 타거나 어쨌든 += 1
    
    answer = count
    return answer
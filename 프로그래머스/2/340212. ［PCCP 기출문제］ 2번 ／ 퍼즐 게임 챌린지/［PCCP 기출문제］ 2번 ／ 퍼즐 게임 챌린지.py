def solution(diffs, times, limit):
    max_level = max(diffs)
    answer = max_level
    left = 1
    right = max_level
    
    
    while left < right:
        level = int((left+right)/2)
        time = 0
        
        for i, diff in enumerate(diffs):
            if level >= diff:
                time += times[i]
            else:
                time += ((sum(times[i-1:i+1])*(diff-level)) + times[i])
        
        if time <= limit:
            right = level
            answer = level
        
        else:
            left = level + 1
        
    return answer
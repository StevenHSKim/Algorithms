def solution(clothes):
    answer = 1
    hash = {}
    
    for name, category in clothes:
        if category in hash.keys():
            hash[category] += [name]
        else:
            hash[category] = [name]
        
    for k,v in hash.items():
        answer *= (len(v)+1)
    
    return answer-1
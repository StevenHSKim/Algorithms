from itertools import permutations

def solution(k, dungeons):
    new_dungeons = permutations(dungeons, len(dungeons))
    result_arr = []
    
    for i in new_dungeons:
        result = 0
        hp = k
        
        for j in range(len(i)):
            if hp >= i[j][0]:
                hp -= i[j][1]
                result += 1
        
        result_arr.append(result)
        
    return max(result_arr)
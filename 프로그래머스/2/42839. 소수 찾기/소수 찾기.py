from itertools import permutations

def solution(numbers):
    num = []
    result = []
    num_arr = list(numbers)
    
    for i in range(1,len(num_arr)+1):
        num += list(permutations(num_arr, i))
    
    num = [int(''.join(n)) for n in num]
    num = list(set(num))
    
    for j in num:
        if j < 2:
            continue
    
        prime = True
        for k in range(2,int(j**0.5)+1):
            if int(j) % k == 0:
                prime = False
                break
    
        if prime:
            result.append(j)
    
    answer = len(result)
    return answer
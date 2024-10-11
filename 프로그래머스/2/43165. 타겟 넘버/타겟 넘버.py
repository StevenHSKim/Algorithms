from itertools import product

def solution(numbers, target):
    answer = 0
    operator = [-1, 1]
    
    for i in product(operator, repeat=len(numbers)):
        total_sum = 0
        for op, num in zip(i, numbers):
            total_sum += op * num
        
        if total_sum == target:
            answer += 1
            
    return answer

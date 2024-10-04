from itertools import combinations_with_replacement

def solution(brown, yellow):
    answer = []
    divisors = []
    
    for i in range(1, yellow+1):
        if yellow % i == 0:
            divisors.append(i)
        
    for i,j in combinations_with_replacement(divisors,2):
        if i*j == yellow and ((i+j)*2)+4 == brown:
            answer.append(i+2)
            answer.append(j+2)
    
    answer.sort(reverse=True)
    return answer
from itertools import product

def solution(word):
    answer = []
    
    li = ['A', 'E', 'I', 'O', 'U']
    
    for i in range(1,6):
        for p in product(li, repeat=i):
            answer.append(''.join(p))
            
    answer.sort()
    return answer.index(word)+1
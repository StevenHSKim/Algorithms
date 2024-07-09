import sys

T = int(input())

for _ in range(T):
    result = sys.stdin.readline().strip()
    score = 0
    sumScore = 0
        
    for i in result:
        if i == 'O':
            score += 1
        else:
            score = 0
        sumScore += score
    
    print(sumScore)
            
import sys

C = int(sys.stdin.readline().rstrip())

for _ in range(C):
    data = list(map(int, sys.stdin.readline().strip().split()))
    N = data[0]
    scores = data[1:]
    
    avg_score = sum(scores)/N
    count = 0
    
    for s in scores:
        if s > avg_score:
            count += 1
            
    ratio = (count/N) * 100
    
    print(f"{ratio:.3f}%")
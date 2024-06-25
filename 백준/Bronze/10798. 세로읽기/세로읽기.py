import sys

word = [sys.stdin.readline().rstrip() for _ in range(5)]
    
for j in range(15):
    for i in range(5):
        if j < len(word[i]):
            print(word[i][j], end='')
N = int(input())
cnt = N

for i in range(N):
    w = input()
    
    for j in range(len(w)-1):
        if w[j] == w[j+1]:
            pass
        
        # 앞으로의 단어에 현재 단어가 포함되어 있나
        elif w[j] in w[j+1:]: 
            cnt -= 1
            break
            
print(cnt)
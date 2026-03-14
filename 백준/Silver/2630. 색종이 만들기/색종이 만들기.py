N = int(input())

paper = []

for _ in range(N):
    row = map(int, input().split())
    row = list(row)
    paper.append(row)


def divide(x,y,size):
    first = paper[x][y]

    for i in range(x,x+size):
        for j in range(y,y+size):
            if paper[i][j] != first: # 돌면서 첫 셀 색이랑 다르면
                half = size//2       # 반으로 또 자르기

                w1,b1 = divide(x,y,half)
                w2,b2 = divide(x,y+half,half)
                w3,b3 = divide(x+half,y,half)
                w4,b4 = divide(x+half,y+half,half)

                return w1+w2+w3+w4, b1+b2+b3+b4
            
    if first == 0:
        return 1,0
    else:
        return 0,1
    
white, blue = divide(0,0,N)
print(white)
print(blue)
N = int(input())
matrix = []
for _ in range(N):
    matrix.append(input().strip())
    
def quadtree(x, y, size):
    first = matrix[x][y]
    
    for i in range(x, x+size):
        for j in range(y, y+size):
            if matrix[i][j]!= first:
                half = size//2
                return "(" + \
                        quadtree(x,y,half) + \
                        quadtree(x,y+half,half) + \
                        quadtree(x+half,y,half) + \
                        quadtree(x+half,y+half,half) + \
                        ")"
    
    return first

print(quadtree(0,0,N))
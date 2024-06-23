N = int(input())

for i in range(1,N):
    ast = "*"*(2*i-1)
    space = " "*(N-i)
    print(space+ast)
    
for i in range(N,0,-1):
    ast = "*"*(2*i-1)
    space = " "*(N-i)
    print(space+ast)
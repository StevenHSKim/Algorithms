N = int(input())

for i in range(N):
    space = " " * (N-i-1)
    star = "*" * (i+1)
    print(space + star)
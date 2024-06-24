N,M = map(int, input().split())

arr_A = []
arr_B = []

for _ in range(N):
    row = list(map(int, input().split()))
    arr_A.append(row)

for _ in range(N):
    row = list(map(int, input().split()))
    arr_B.append(row)
    
for row in range(N):
    for col in range(M):
        print(arr_A[row][col]+ arr_B[row][col], end=' ')
    print()
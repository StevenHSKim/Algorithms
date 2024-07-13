N = int(input())

arr = list(map(int, input().split()))

cnt = 0
for i in arr:
    output_arr = []
    for j in range(2, i+1):
        if i % j == 0:
            output_arr.append(j)
        
    if len(output_arr) == 1:
        cnt += 1
    
print(cnt)
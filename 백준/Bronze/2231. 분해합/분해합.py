N = int(input())

arr = []
for i in range(N):
    sum = i
    for j in str(i):
        sum += int(j)
        
    if sum == N:
        arr.append(i)

arr = sorted(arr)
if len(arr) == 0:
    print(0)
else:
    print(arr[0])
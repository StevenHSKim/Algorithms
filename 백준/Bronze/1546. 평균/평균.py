N = int(input())
arr = list(map(int, input().split()))

M = max(arr)
new_arr = []

for i in arr:
    new_arr.append(i/(M*100))

mean = sum(new_arr)/len(new_arr)

print(mean*10000)
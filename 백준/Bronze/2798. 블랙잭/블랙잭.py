from itertools import combinations

N,M = map(int, input().split())
arr = list(map(int, input().split()))

biggest_sum = 0
for i in combinations(arr,3):
    temp_sum = sum(i)
    if biggest_sum < temp_sum <= M:
        biggest_sum = temp_sum

print(biggest_sum)
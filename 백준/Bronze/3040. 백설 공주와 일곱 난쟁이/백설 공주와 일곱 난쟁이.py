from itertools import combinations

num_list = []
for _ in range(9):
    n = int(input())
    num_list.append(n)

for comb in combinations(num_list, 7):
    if sum(comb) == 100:
        for i in comb:
            print(i)
        break
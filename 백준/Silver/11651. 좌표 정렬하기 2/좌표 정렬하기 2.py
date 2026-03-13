N = int(input())

n_list = []
for i in range(N):
    n = input().split()
    n = map(int, n)
    n = list(n)
    n_list.append(n)

n_list.sort(key=lambda x:(x[1],x[0]))

for i in n_list:
    print(*i)
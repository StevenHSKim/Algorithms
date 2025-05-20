import sys

N = int(sys.stdin.readline().strip())
N_list = sorted(list(map(int, sys.stdin.readline().strip().split())))
    
M = int(sys.stdin.readline().strip())
M_list = list(map(int, sys.stdin.readline().strip().split()))
    
dic = {}
for i in N_list:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    
    if array[mid] == target:
        return dic[target]
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

for j in M_list:
    print(binary_search(N_list, j, 0, N-1), end=" ")
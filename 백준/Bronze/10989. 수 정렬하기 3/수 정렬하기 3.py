import sys

N = int(input())
num_list = [0] * 10001

for _ in range(N):
    a = int(sys.stdin.readline())
    num_list[a] += 1
    
for i in range(len(num_list)):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)
T = int(input())

for _ in range(T):
    R, S = input().split()
    for i in range(len(S)):
        print(int(R) * S[i], end='')
    print()
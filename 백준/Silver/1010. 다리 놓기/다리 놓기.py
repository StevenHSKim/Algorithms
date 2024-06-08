import math
N = int(input())

for _ in range(N):
    A,B = map(int,input().split())
    output = math.factorial(B) / (math.factorial(B-A) * math.factorial(A))
    print(int(output))
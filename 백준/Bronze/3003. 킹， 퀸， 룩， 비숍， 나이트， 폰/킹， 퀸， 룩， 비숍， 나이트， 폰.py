A =list(map(int,input().split()))
B = [1, 1, 2, 2, 2, 8]


output_list = [B[i]-A[i] for i in range(len(A))]
print(*output_list)
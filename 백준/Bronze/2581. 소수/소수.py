M = int(input())
N = int(input())

prime_arr = []
for i in range(M, N+1):
    arr = []
    for j in range(2, i+1):
        if i % j == 0:
            if i == j:
                prime_arr.append(i)
            break

if len(prime_arr) == 0:
    print("-1")
else:
    print(sum(prime_arr))
    print(prime_arr[0])
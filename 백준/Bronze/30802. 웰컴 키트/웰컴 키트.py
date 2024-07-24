N = int(input())
arr = list(map(int, input().split()))
T,P = map(int, input().split())

Tshirts_sum = 0
for i in arr:
    if i%T == 0:
        Tshirts_sum += i//T
    else:
        Tshirts_sum += i//T+1
        
print(Tshirts_sum)
print(f"{N//P} {N%P}")
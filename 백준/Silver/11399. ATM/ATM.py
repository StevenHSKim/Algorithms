N = int(input())
list1 = list(map(int,input().split()))
list1.sort()
    
output = 0
for i in list1:
    output += i * N
    N -= 1

print(output)
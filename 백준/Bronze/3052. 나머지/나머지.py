import sys

arr = []

for i in range(10):
    a = int(sys.stdin.readline())
    remainder = a%42
    
    if remainder not in arr:
        arr.append(remainder)

print(len(arr))
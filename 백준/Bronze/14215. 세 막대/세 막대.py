arr = sorted(list(map(int, input().split())))

while True:
    if arr[2]>=arr[0]+arr[1]:
        x = arr.pop(-1)
        arr.append(x-1)
        arr = sorted(arr)
    else:
        break

print(sum(arr))
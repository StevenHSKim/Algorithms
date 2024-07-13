x,y,w,h = map(int, input().split())

arr = []

arr.append(x)
arr.append(y)
arr.append(w-x)
arr.append(h-y)

print(sorted(arr)[0])
arr = list(map(int,input().split()))
sorted_arr = sorted(arr)

if arr == sorted_arr:
    print("ascending")
    
elif arr == list(reversed(sorted_arr)):
    print("descending")
    
else:
    print("mixed")

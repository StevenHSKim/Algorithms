while True:
    arr = sorted(list(map(int, input().split())))
    if arr[0]==arr[1]==arr[2]==0:
        break
    else:
        if arr[2]**2 == arr[0]**2 + arr[1]**2:
            print("right")
        else:
            print("wrong")
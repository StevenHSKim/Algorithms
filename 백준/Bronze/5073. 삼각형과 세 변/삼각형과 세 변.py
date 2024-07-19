while True:
    a,b,c = map(int, input().split())
    arr = sorted([a,b,c])
    
    if a==b==c==0:
        break
    else:
        if arr[2] >= arr[0] + arr[1]:
            print("Invalid")
        else:
            if a==b==c:
                print("Equilateral")
            elif a==b or b==c or a==c:
                print("Isosceles")
            else:
                print("Scalene")        
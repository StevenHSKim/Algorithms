while True:
    n = int(input())
    
    if n == -1:
        break
    
    else:
        arr = []
        for i in range(1,n+1):
            if n % i == 0:
                arr.append(i)
                
        str_arr = list(map(str, arr))
        
        if 2*n == sum(arr):
            print(f"{n} = {' + '.join(str_arr[:-1])}")
        else:
            print(f"{n} is NOT perfect.")
x_arr = []
y_arr = []

for i in range(3):
    x,y = input().split()
    
    if x in x_arr:
        if y in y_arr:
            x_arr.remove(x)
            y_arr.remove(y)
        else:
            x_arr.remove(x)
            y_arr.append(y)
    
    elif y in y_arr:
        y_arr.remove(y)
        x_arr.append(x)
        
    else:
        x_arr.append(x)
        y_arr.append(y)

print(f"{x_arr[0]} {y_arr[0]}")
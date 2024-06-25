matrix = []
row_max_arr = []

for row in range(9):
    
    row = list(map(int,input().split()))
    matrix.append(row)
    
    row_max = max(row)
    row_max_arr.append(row_max)
    

max_val = max(row_max_arr) 
max_row_index = row_max_arr.index(max_val)
max_col_index = matrix[max_row_index].index(max_val)

print(max_val)
print(f"{max_row_index+1} {max_col_index+1}") # row col
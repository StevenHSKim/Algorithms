def solution(array, commands):
    answer = []
    
    for i in commands:
        sliced_arr = array[i[0]-1:i[1]]
        sliced_arr.sort()
        answer.append(sliced_arr[i[2]-1])
    return answer
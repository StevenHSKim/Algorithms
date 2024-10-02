def solution(numbers):
    answer = ''
    
    str_numbers = [str(num) for num in numbers]
    str_numbers.sort(key = lambda x:x*3, reverse=True)
    
    for i in str_numbers:
        answer += i
        
    return str(int(answer))
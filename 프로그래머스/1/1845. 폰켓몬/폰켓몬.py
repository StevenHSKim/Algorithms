def solution(nums):
    half = len(nums) // 2
    length = len(set(nums))
    
    if half <= length:
        answer = half
    else:
        answer = length
    
    return answer
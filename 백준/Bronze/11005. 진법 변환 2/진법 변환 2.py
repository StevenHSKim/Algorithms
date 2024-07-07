N,B = map(int, input().split())
number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = ''

while N: # 나눠질때까지 (N>0일 때까지)
    result += str(number[N%B]) # B진수로 숫자 N을 나눈 나머지를 기록
    N //= B # 한번 나눴으니 몫으로 N을 업데이트
    
print(result[::-1])
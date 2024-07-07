N, B = input().split()
B = int(B)

number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' # 0부터 넣기 주의

result = 0

# enumerate: 인덱스와 원소 동시 접근
for i, num in enumerate(N[::-1]): # N을 거꾸로 -> 가장 마지막에 있는 숫자가 0승부터 시작하므로                        
    result += number.index(num) * (B ** i)  # 해당 자리수 x (진수 ** 자리수)
    # ex) 이진수 1010 -> (1x2^3) + (0x2^2) + (1x2**1) + (0x2**0)

print(result)
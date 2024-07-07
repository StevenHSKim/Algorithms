# while문 사용하면 시간 초과

A,B,V = map(int, input().split())

# (A*day) - (B*(day-1)) >= V
# 기존의 위 식을 day를 기준으로 전개하면
# day >= (V-A)/(A-V) 이다.

day = (V-B)/(A-B) # float로 나옴

if day == int(day):  # day가 정수로 떨어지는 경우 -> 그대로
    print(int(day))
else:                # day가 4.1일인 경우 -> 5일 소요
    print(int(day)+1)
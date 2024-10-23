N,K = map(int, input().split())
numerator = N    # 분자
denominator = K  # 분모
numerator_result = 1
denominator_result = 1

for _ in range(K):
    numerator_result *= numerator
    numerator = numerator - 1
    
    denominator_result *= denominator
    denominator = denominator - 1
    
print(int(numerator_result / denominator_result))
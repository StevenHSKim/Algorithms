N = int(input())

num_box = 2 ** (N*2)

result = (num_box**(1/2)+1) ** 2

print(int(result))
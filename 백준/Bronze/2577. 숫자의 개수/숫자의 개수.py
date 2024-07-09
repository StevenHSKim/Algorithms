A = input()
B = input()
C = input()

num = int(A) * int(B) * int(C)

for i in range(10):
    print(str(num).count(str(i)))
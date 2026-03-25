X = int(input())

stick = [64, 32, 16, 8, 4, 2, 1]
count = 0

for i in stick:
    if i <= X:
        X -= i
        count += 1
    if X == 0:
        print(count)
        break
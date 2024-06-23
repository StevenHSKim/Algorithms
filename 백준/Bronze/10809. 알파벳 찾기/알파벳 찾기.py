S = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
output = []

for i in alphabet:
    if i in S:
        output.append(S.index(i))
    else:
        output.append(-1)
        
print(*output)
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

alphabet = list(input())
sec = 0

for i in alphabet:
    for j in dial:
        if i in str(j):
            num = dial.index(j) + 3
            sec += num
print(sec)
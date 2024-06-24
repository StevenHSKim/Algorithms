clist = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

S = input()
cnt = 0

for i in clist:
    if i in S:
        S = S.replace(i,"!")

print(len(S))
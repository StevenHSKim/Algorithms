A,B,C = map(int,input().split())

if A == B == C:
    print(A*1000+10000)
elif A != B and B != C and C != A:
    if A > B and A > C:
        print(A*100)
    elif B > A and B > C:
        print(B*100)
    else:
        print(C*100)
else:
    if A == B:
        print(A*100 + 1000)
    elif A == C:
        print(A*100 + 1000)
    else:
        print(B*100 + 1000)
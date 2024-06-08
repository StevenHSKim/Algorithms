H,M = map(int, input().split())
A = int(input())

if M+A < 60:
    print(f"{H} {M+A}")
elif M+A >= 60:
    if (A%60)+M >= 60:
        if H+(A//60)+1 < 24:
            print(f"{H+(A//60)+1} {M+(A%60)-60}")
        else:
            print(f"{H+(A//60)-23} {M+(A%60)-60}")
    else:    
        if H+(A//60) < 24:
            print(f"{H+(A//60)} {M+(A%60)}")
        else:
            print(f"{H+(A//60)-24} {M+(A%60)}")
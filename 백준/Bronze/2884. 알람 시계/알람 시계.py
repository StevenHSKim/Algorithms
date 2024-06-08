H,M = map(int, input().split())

if M >= 45:
    print(f"{H} {M-45}")
else:
    if H >= 1:
        print(f"{H-1} {M+15}")
    else:
        print(f"{H+23} {M+15}")
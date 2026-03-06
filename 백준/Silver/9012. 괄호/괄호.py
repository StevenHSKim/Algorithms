N = int(input())

for _ in range(N):
    stack = []
    parenthesis = input().strip()
    is_vps = True
    
    for i in range(len(parenthesis)):
        if parenthesis[i] == "(":
            stack.append("(")
        else:   # if parenthesis[i] == ")"
            if len(stack) != 0:
                stack.pop()
            else:
                is_vps = False
                break
    
    if is_vps and len(stack) == 0:
        print("YES")
    else:
        print("NO")
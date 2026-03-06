parentheses = input().strip()
stack = []
answer = 0

for i in range(len(parentheses)):
    if parentheses[i] == '(':
        stack.append('(')
    else: # parentheses[i] == ')'
        if parentheses[i-1] == '(':
            stack.pop()
            answer += len(stack)
        else: # parentheses[i-1] == ')'
            stack.pop()
            answer += 1
            
print(answer)


N = int(input())

def star(N):
    if N == 3:
        return ['***', '* *', "***"]

    prev = star(N//3)
    result = []
    
    for s in prev:
        result.append(s*3)
    for s in prev:
        result.append(s + ' '*(N//3) + s)
    for s in prev:
        result.append(s*3)

    return result

print('\n'.join(star(N)))
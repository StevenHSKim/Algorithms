def solution(sizes):
    w = []
    h = []
    
    for i,j in sizes:
        if i >= j:
            w.append(i)
            h.append(j)
        else:
            w.append(j)
            h.append(i)
    
    answer = max(w) * max(h)
    return answer
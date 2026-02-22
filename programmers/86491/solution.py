def solution(sizes):
    bigs = []
    smalls = []
    
    for w, h in sizes:
        if w >= h:
            bigs.append(w)
            smalls.append(h)
        else:
            bigs.append(h)
            smalls.append(w)
            
    return max(bigs) * max(smalls)
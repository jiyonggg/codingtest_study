def solution(n, lost, reserve):
    real_reserve = sorted(set(reserve) - set(lost))
    real_lost = sorted(set(lost) - set(reserve))

    for r in real_reserve:
        if (r-1) in real_lost:
            real_lost.remove(r-1)
        elif (r+1) in real_lost:
            real_lost.remove(r+1)
    
    return n - len(real_lost)
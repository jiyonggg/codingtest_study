def solution(citations):
    for h in range(min(max(citations), 1000), -1, -1):
        if len(list(filter(lambda x: x >= h, citations))) >= h:
            return h
    
    return 0
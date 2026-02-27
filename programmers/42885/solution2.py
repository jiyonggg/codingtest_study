def solution(people, limit):
    people.sort(reverse=True)
    max_idx = 0
    min_idx = len(people) - 1
    
    cnt = 0

    while max_idx < min_idx:
        if people[max_idx] + people[min_idx] <= limit:
            min_idx -= 1
        
        max_idx += 1
        cnt += 1
    
    if max_idx == min_idx:
        cnt += 1
    
    return cnt
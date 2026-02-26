def dfs(start, unvisited, distance, name_length, current_min):
    if distance >= current_min:
        return current_min # None 대신 기존 최솟값을 return해서 가지치기를 구현
    
    if not unvisited:
        return distance
    
    nearest_next = unvisited[0]
    nearest_prev = unvisited[-1]

    nearest_next_min = min(abs(start-nearest_next), name_length-abs(start-nearest_next))
    nearest_prev_min = min(abs(start-nearest_prev), name_length-abs(start-nearest_prev))

    current_min = dfs(nearest_next, unvisited[1:], distance+nearest_next_min, name_length, current_min)
    current_min = dfs(nearest_prev, unvisited[:-1], distance+nearest_prev_min, name_length, current_min)

    return current_min

def solution(name):
    updown_cnt = 0
    unvisited = []
    
    for idx, char in enumerate(name):
        if char == 'A':
            continue

        updown_cnt += min(ord(char)-ord('A'), ord('Z')-ord(char)+1)
        
        if idx:
            unvisited.append(idx)

    answer = updown_cnt + dfs(0, unvisited, 0, len(name), 100000)
    return answer
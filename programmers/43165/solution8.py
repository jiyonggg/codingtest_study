from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    
    queue.append((0, 0))

    while queue:
        idx, curr_sum= queue.popleft()

        if idx == len(numbers):
            if curr_sum == target:
                answer += 1
            continue
        
        queue.append((idx+1, curr_sum+numbers[idx]))
        queue.append((idx+1, curr_sum-numbers[idx]))
        
    return answer
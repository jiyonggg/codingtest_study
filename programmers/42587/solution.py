from collections import deque

def solution(priorities, location):
    process_queue = deque()
    
    for idx, priority in enumerate(priorities):
        process_queue.append((idx, priority))

    priorities.sort()

    answer = 0
    
    while process_queue:
        process = process_queue.popleft()

        if process[1] == priorities[-1]:
            answer += 1
            priorities.pop()

            if process[0] == location:
                return answer
        else:
            process_queue.append(process)
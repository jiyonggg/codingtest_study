def solution(numbers, target):
    answer = 0
    stack = [(0, 0)]

    while stack:
        idx, curr_sum= stack.pop()

        if idx == len(numbers):
            if curr_sum == target:
                answer += 1
            continue
        
        stack.append((idx+1, curr_sum+numbers[idx]))
        stack.append((idx+1, curr_sum-numbers[idx]))
        
    return answer
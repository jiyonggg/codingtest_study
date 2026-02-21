answer = 0

def dfs(numbers, depth, target, stack):
    global answer

    if depth == len(numbers):
        if sum(stack) == target:
            answer += 1
        return

    curr_minus = numbers[depth] * -1
    curr_plus = numbers[depth]

    dfs(numbers, depth+1, target, stack+[curr_minus])
    dfs(numbers, depth+1, target, stack+[curr_plus])

def solution(numbers, target):
    first_minus = numbers[0] * -1
    first_plus = numbers[0]

    dfs(numbers, 1, target, [first_minus])
    dfs(numbers, 1, target, [first_plus])

    return answer
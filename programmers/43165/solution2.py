def solution(numbers, target):
    if not numbers and not target:
        return 1
    elif not numbers:
        return 0

    return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
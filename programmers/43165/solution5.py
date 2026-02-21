from itertools import combinations

def solution(numbers, target):
    goal = sum(numbers) - target
    answer = 0

    for i in range(len(numbers)):
        combs = combinations(range(len(numbers)), i)
        for comb in combs:
            tmp = 0

            for idx in comb:
                tmp += (numbers[idx] * 2)
            if goal == tmp:
                answer += 1
    
    return answer
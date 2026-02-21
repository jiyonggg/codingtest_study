from itertools import product

def solution(numbers, target):
    tmp = [(number*-1, number) for number in numbers]
    return list(map(sum, product(*tmp))).count(target)
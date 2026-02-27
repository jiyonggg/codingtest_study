from itertools import permutations
from math import floor

def solution(numbers):
    nums = set()

    for i in range(1, len(numbers)+1):
        nums |= set(map(lambda x: int("".join(x)), permutations(numbers, i)))

    # 0, 1은 소수가 아님
    nums -= set(range(2))

    # 에라토스테네스의 체
    for i in range(2, floor(max(nums)**0.5)+1):
        nums -= set(range(i*2, max(nums)+1, i))

    return len(nums)
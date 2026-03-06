from functools import lru_cache

def solution(triangle):
    n = len(triangle) - 1

    @lru_cache
    def find_max(level, index):
        nonlocal n, triangle

        if level == n:
            return triangle[level][index]
        
        return triangle[level][index] + max(find_max(level+1, index), find_max(level+1, index+1))
    
    return find_max(0, 0)
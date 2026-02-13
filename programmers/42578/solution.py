from collections import defaultdict

def solution(clothes):
    clothes_map = defaultdict(list)

    for cloth, type in clothes:
        clothes_map[type].append(cloth)
    
    result = 1

    for key in clothes_map:
        result *= (len(clothes_map[key]) + 1)
    
    result -= 1

    return result
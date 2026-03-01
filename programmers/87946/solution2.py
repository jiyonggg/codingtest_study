from itertools import permutations

def solution(k, dungeons):
    result = 0

    for case in permutations(range(len(dungeons))):
        curr_fatigue = k
        cnt = 0

        for num in case:
            require, consume = dungeons[num]

            if curr_fatigue >= require:
                cnt += 1
                curr_fatigue -= consume
        
        result = max(result, cnt)
    
    return result
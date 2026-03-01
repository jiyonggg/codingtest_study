def explore_dungeon(dungeons, k, cnt):
    can_enter = list(filter(lambda x: x[0] <= k, dungeons))

    result = 0

    if not can_enter:
        return cnt
    else:
        for i in range(len(dungeons)):
            require, consume = dungeons[i]

            if require <= k:
                result = max(result, explore_dungeon(dungeons[:i]+dungeons[i+1:], k-consume, cnt+1))
        
    return result

def solution(k, dungeons):
    return explore_dungeon(dungeons, k, 0)